import copy
class Node:
    def __init__(self, name, weight):
        self.name = name  # 节点名
        self.weight = weight  # 节点权重
        self.left = None  # 节点左孩子
        self.right = None  # 节点右孩子
        self.father = None  # 节点父节点
    #判断是否是左孩子

    def is_left_child(self):
        return self.father.left == self

#创建最初的叶子节点


def create_prim_nodes(data_set, labels):
    if(len(data_set) != len(labels)):
        raise Exception('data is not lined up with lables!')
    nodes = []
    for i in range(len(labels)):
        nodes.append(Node(labels[i], data_set[i]))
    return nodes


# 创建huffman树
def create_HF_tree(nodes):
    #此处注意，copy()属于浅拷贝，只拷贝最外层元素，内层嵌套元素则通过引用，而不是独立分配内存
    tree_nodes = nodes.copy()
    while len(tree_nodes) > 1:  # 只剩根节点时，退出循环
        tree_nodes.sort(key=lambda node: node.weight)  # 升序排列
        new_left = tree_nodes.pop(0)
        new_right = tree_nodes.pop(0)
        new_node = Node(None, (new_left.weight + new_right.weight))
        new_node.left = new_left
        new_node.right = new_right
        new_left.father = new_right.father = new_node
        tree_nodes.append(new_node)
    tree_nodes[0].father = None  # 根节点父亲为None
    return tree_nodes[0]  # 返回根节点

#获取huffman编码


def get_huffman_code(root, nodes):
    codes = {}
    for node in nodes:
        code = ''
        name = node.name
        while node.father != None:
            if node.is_left_child():
                code = '0' + code
            else:
                code = '1' + code
            node = node.father
        codes[name] = code
    return codes

from collections import Counter

if __name__ == "__main__":
    test_data = str(555)
    labels = list(set(test_data))
    c = Counter(test_data)
    dataset = list(c.values())
    nodes = create_prim_nodes(dataset, labels)
    root = create_HF_tree(nodes)
    codes = get_huffman_code(root, nodes)
    for key in codes.keys():
        if codes[key] == '':
            print(key, 0)
        else:
            print(f'{key}: {codes[key]}')
