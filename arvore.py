class Arvore:
    def _init_(self, key):
        self.left = None
        self.right = None
        self.val = key

def insira(root, key):
    if root is None:
        return Arvore(key)
    else:
        if key < root.val:
            root.left = insira(root.left, key)
        else:
            root.right = insira(root.right, key)
    return root

def numero_ordem(root):
    if root:
        numero_ordem(root.left)
        print(root.val, end=" ")
        numero_ordem(root.right)

def numero_decrescente(root):
    if root:
        print(root.val, end=" ")
        numero_decrescente(root.left)
        numero_decrescente(root.right)

def numero_crescente(root):
    if root:
        numero_crescente(root.left)
        numero_crescente(root.right)
        print(root.val, end=" ")

def procura(root, key):
    if root is None or root.val == key:
        return root

    if root.val < key:
        return procura(root.right, key)

    return procura(root.left, key)

def encontrar_maior(root):
    while root.right is not None:
        root = root.right
    return root.val

def  encontrar_menor(root):
    while root.left is not None:
        root = root.left
    return root.val

def encontrar_soma(root):
    if root is None:
        return 0
    return root.val + encontrar_soma(root.left) + encontrar_soma(root.right)

def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def contar_no(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return contar_no(root.left) + contar_no(root.right)

def encontar_numero(root):
    if root is None:
        return -1
    left_height = encontar_numero(root.left)
    right_height = encontar_numero(root.right)
    return max(left_height, right_height) + 1

def encontar_media(root):
    if root is None:
        return 0
    total_sum = encontrar_soma(root)
    total_nodes = count_nodes(root)
    return total_sum / total_nodes if total_nodes != 0 else 0

root = None
root = insira(root, 7)
root = insira(root, 3)
root = insira(root, 9)
root = insira(root, 1)
root = insira(root, 5)

print("Imprimindo os valores:")
numero_ordem(root)
print("\nNúmeros em ordem decrescente:")
numero_decrescente(root)
print("\nNúmeros em ordem crescente:")
numero_crescente(root)
print("\nProcurar o número 9:", procura(root, 9) is not None)
print("Maior valor:",encontrar_maior(root))
print("Menor valor:", encontrar_menor(root))
print("Valor médio:", encontar_media(root))
print("Somando os valor:", encontrar_soma(root))
print("Número de nó:", contar_no(root))
print("Altura da Árvore:", encontar_numero(root))
