import { useState, useEffect } from 'preact/hooks';

const FAKE_STORE_API = 'https://fakestoreapi.com/products';
let model = null;

async function loadModel() {
  model = await tf.loadLayersModel('https://storage.googleapis.com/tfjs-models/tfjs/mobilenet_v1_0.25_224/model.json');
}

const ProductCard = ({ product, onClick, isRecommendation = false }) => (
  <div class="card m-2">
    <div class="card-image">
      <figure class="image is-4by3">
        <img 
          src={product.image} 
          alt={product.title}
          crossorigin="anonymous"
          style="object-fit: contain; padding: 1rem;"
        />
      </figure>
    </div>
    <div class="card-content">
      <p class="title is-5">{product.title}</p>
      <p class="subtitle is-6">${product.price}</p>
      <p class="subtitle is-6">{product.category}</p>
      {!isRecommendation && (
        <button class="button is-primary" onClick={() => onClick(product)}>
          View Similar
        </button>
      )}
    </div>
  </div>
);

export function App() {
  const [products, setProducts] = useState([]);
  const [selectedProduct, setSelectedProduct] = useState(null);
  const [recommendations, setRecommendations] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    Promise.all([
      loadModel(),
      fetchProducts()
    ]);
  }, []);

  const fetchProducts = async () => {
    try {
      const response = await fetch(FAKE_STORE_API);
      const data = await response.json();
      setProducts(data);
    } catch (error) {
      console.error('Error fetching products:', error);
    }
  };

  const findSimilarProducts = async (product) => {
    setIsLoading(true);
    try {
      // Get products from same category first
      const sameCategoryProducts = products.filter(p => 
        p.id !== product.id && p.category === product.category
      );

      // Then get products from other categories
      const otherProducts = products.filter(p => 
        p.id !== product.id && p.category !== product.category
      );

      // Simple text-based similarity
      const calculateSimilarity = (p1, p2) => {
        const cat = p1.category === p2.category ? 1 : 0;
        const desc = (p1.description || '').toLowerCase().split(' ')
          .filter(word => (p2.description || '').toLowerCase().includes(word)).length;
        return cat * 0.5 + (desc / 100) * 0.5;
      };

      // Combine and sort by similarity
      const similarProducts = [...sameCategoryProducts, ...otherProducts]
        .slice(0, 6)
        .map(p => ({
          ...p,
          similarity: calculateSimilarity(product, p)
        }))
        .sort((a, b) => b.similarity - a.similarity)
        .slice(0, 3);

      setRecommendations(similarProducts);
    } catch (error) {
      console.error('Error finding similar products:', error);
      // Fallback to category-based recommendations
      const fallbackRecs = products
        .filter(p => p.id !== product.id && p.category === product.category)
        .slice(0, 3);
      setRecommendations(fallbackRecs);
    }
    setIsLoading(false);
  };

  const handleProductClick = (product) => {
    setSelectedProduct(product);
    findSimilarProducts(product);
  };

  return (
    <div class="container mt-5 px-3">
      <h4 class="title is-2 has-text-centered mb-5">Product Recommendation w/ tf.js</h4>
      
      {products.length === 0 ? (
        <div class="has-text-centered">
          <div class="loader"></div>
          <p>Loading products...</p>
        </div>
      ) : (
        <div class="columns is-multiline">
          {products.map(product => (
            <div class="column is-one-third" key={product.id}>
              <ProductCard product={product} onClick={handleProductClick} />
            </div>
          ))}
        </div>
      )}

      {isLoading && (
        <div class="has-text-centered mt-4">
          <div class="loader"></div>
          <p>Finding similar products...</p>
        </div>
      )}

      {selectedProduct && recommendations.length > 0 && (
        <div class="mt-6">
          <h2 class="title is-4">Similar to {selectedProduct.title}</h2>
          <div class="columns">
            {recommendations.map(product => (
              <div class="column is-one-third" key={product.id}>
                <ProductCard 
                  product={product} 
                  onClick={handleProductClick}
                  isRecommendation={true}
                />
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}