### Frequently Asked Questions

1. What is the aim of this project?

The goal is to build a lightweight, client-side recommendation system that suggests visually similar products using image-based similarity instead of traditional user behavior analysis.

2. How does the recommendation system work?

It uses MobileNet (a pre-trained deep learning model) to extract feature embeddings from product images. The system then calculates cosine similarity between these embeddings to find the most visually similar products.

3. What technologies are used in this project?

- TensorFlow.js – Runs MobileNet in the browser for real-time image processing.
- FakeStoreAPI – Provides mock product data (images, descriptions, prices, etc.).
- JavaScript, HTML, and CSS – Frontend implementation for the recommendation UI.

4. Why use MobileNet for this project?

MobileNet is a lightweight convolutional neural network (CNN) optimized for mobile and web applications. It provides fast, efficient feature extraction while maintaining good accuracy, making it ideal for image similarity tasks.

5. Why is TensorFlow.js used instead of Python-based frameworks like TensorFlow or PyTorch?

TensorFlow.js allows the entire recommendation system to run directly in the user’s browser without requiring a backend server. This ensures:

- Lower latency (no server calls needed).
- Better privacy (no user data sent to external servers).
- Cross-platform compatibility (runs on any device with a browser).


6. What is FakeStoreAPI, and why is it used?

FakeStoreAPI is a free e-commerce API that provides mock product data like images, categories, prices, and descriptions. It helps prototype recommendation systems without needing a real database.

7. What kind of recommendations does this system provide?

The system recommends products based on visual similarity—meaning users see items that look similar to their selected product rather than recommendations based on **user behavior or purchase history.**

8. How accurate are the recommendations?

Since MobileNet is pre-trained on general image data, recommendations are fairly accurate for visually similar products. However, fine-tuning with a domain-specific dataset could improve results.

9. What are the key advantages of this project?

- Fully client-side – No backend required, making it fast and private.
- Lightweight & efficient – Uses MobileNet and TensorFlow.js for fast execution.
- Scalable – Can be easily integrated into real e-commerce platforms.
- Easy to extend – Can incorporate more advanced models or hybrid recommendations.

10. What are the future improvements planned for the project?

- Personalized recommendations based on user interactions.
- Hybrid approach combining image similarity with text-based descriptions.
- Integration with real e-commerce APIs for production use.
- Performance optimizations for handling larger datasets.