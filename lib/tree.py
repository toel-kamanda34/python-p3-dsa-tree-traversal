class Tree:
    def __init__(self, root = None):
        self.root = root
    '''
    def get_element_by_id(self, target_id):
        #call helper method (depth_first_traversal) that performs the actual depth-first search
        return self.depth_first_traversal(self.root, target_id)


    def depth_first_traversal(self, node, target_id):
      #if the root node matches the elemnet id return it
        if node is None:
          return None
      
        if node['id'] == target_id:
          return node
      
        for child in node['children']:
          found = self.depth_first_traversal(child, target_id)
          if found:
             return found
          
        return None '''
    def get_element_by_id(self, target_id):
        return self.breadth_first_traversal(self.root, target_id)
    
    def breadth_first_traversal(self, node, target_id):
        if node is None:
            return None
        
        nodes_to_visit = [node]

        while nodes_to_visit:
            current_node = nodes_to_visit.pop(0)

            if current_node['id'] == target_id:
                return current_node
            
            nodes_to_visit.extend(current_node['children'])

        return None
        
          


child_1 = {
  'tag_name': 'h2',
  'id': 'subtitle',
  'text_content': 'Subtitle',
  'children': []
}

child_2 = {
  'tag_name': 'div',
  'id': 'content',
  'text_content': 'Content goes here',
  'children': []
}

root = {
  'tag_name': 'h1',
  'id': 'heading',
  'text_content': 'Title',
  'children': [child_1, child_2]
}


tree = Tree(root)


result = tree.get_element_by_id('content')
print(result)
