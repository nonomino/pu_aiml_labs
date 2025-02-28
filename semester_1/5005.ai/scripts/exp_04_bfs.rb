def bfs(graph, start, goal)
  queue = [[start]]
  visited = [start]

  while queue.any?
    path = queue.shift
    p "The path is currently\n #{path}"
    p "The queue look like: #{queue}"
    node = path.last

    if node == goal
      return path
    end

    graph[node].each do |adjacent|
      unless visited.include?(adjacent)
        visited << adjacent
        queue << path + [adjacent]
      end
    end
  end
end

graph = { '5' => ['3', '7'], '3' => ['2', '4'], '7' => ['8'], '2' => [], '4' => ['8'], '8' => [] }
puts bfs(graph, '5', '8').inspect
