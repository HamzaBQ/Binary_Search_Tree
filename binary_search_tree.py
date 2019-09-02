import random as rd
import pdb
import numpy as np
import pygame
from enum import Enum
import time
import sys


black = 0, 0, 0
white = 255, 255, 255
node_radius = 15
w_margin = 50
h_margin = 50
width = 1300
height = 500


class UnbalancementCase(int, Enum):
    LEFT_LEFT = 0
    LEFT_RIGHT = 1
    RIGHT_RIGHT = 2
    RIGHT_LEFT = 3


# Tree priniting helper function
n_tabs = 0
def print_tabs(n_tabs):
    print(' '*n_tabs, end = '')


def display():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            pygame.display.update()

# Node class 
class Node():
    def __init__(self, key, left = None, right = None, parent = None, coords = None):
        self.right = None
        self.left = None
        self.height = 0
        self.key = key
        self.coords = coords
        self.parent = parent
    
    def draw(self, screen):
        node_coords = self.coords
        node_x = coords_dict[node_coords[0]][node_coords[1]]
        
        node_y = h_margin + y_mov_unit*(node_coords[0] - 1)
        
        color = pygame.Color(179,255,229)
        pygame.draw.circle(screen, color, (int(node_x), int(node_y)), max(10,int(node_radius)))
        
        # Now let's add the corresponding text at the same point 
        font = pygame.font.SysFont('verdana', 14)

        text = font.render(str(self.key), True, black)
        text_rect = text.get_rect()
        text_rect.center = (node_x, node_y)
        screen.blit(text, text_rect)

    
    def draw_branches(self, screen):
        print('*'*10 + 'DRAW BRANCHES' + '*'*10)

        orig_node = self
        orig_coords = self.coords

        if orig_node.left != None:

            orig_x = coords_dict[orig_coords[0]][orig_coords[1]] 
            orig_y = h_margin + y_mov_unit*(orig_coords[0] - 1) + max(10, node_radius)
            
            dest_node = self.left
            dest_coords = dest_node.coords
            dest_x = coords_dict[dest_coords[0]][dest_coords[1]] 
            dest_y = h_margin + y_mov_unit*(dest_coords[0] - 1) - max(10, node_radius)
            left_color = pygame.Color(255, 0, 0)
            pygame.draw.line(screen, left_color, (int(orig_x), int(orig_y)), (int(dest_x), int(dest_y)), 1)

        if self.right != None:
            orig_x = coords_dict[orig_coords[0]][orig_coords[1]] 
            orig_y = h_margin + y_mov_unit*(orig_coords[0] - 1) + max(10, node_radius)
            
            dest_node = self.right
            dest_coords = dest_node.coords

            dest_x = coords_dict[dest_coords[0]][dest_coords[1]] 
            dest_y = h_margin + y_mov_unit*(dest_coords[0] - 1) - max(10, node_radius)

            right_color = pygame.Color(0,255,0)
            pygame.draw.line(screen, right_color, (int(orig_x), int(orig_y)), (int(dest_x), int(dest_y)),  1)
        
        return

# Tree class
class Tree():

    def __init__(self):
        self.root = None
        self.depth = 0


    def insert_key(self, new_key):
        # root emptiness examination
        if self.root == None:
            self.root = Node(new_key)
            new_node = self.root
        else:
            new_node = self.__insert_key(self.root, new_key)
        self.depth = self.root.height
        return new_node
        # update heights of the parents
    

    def __insert_key(self, node, new_key):
        if new_key > node.key:
            if node.right == None:
                node.right = Node(new_key, parent=node)
                new_node = node.right
            else:
                new_node = self.__insert_key(node.right, new_key)
        else:
            if node.left == None:
                node.left = Node(new_key, parent=node)
                new_node = node.left
            else:
                new_node = self.__insert_key(node.left, new_key)
        node.height = 1 + max(node.right.height if node.right != None else 0, node.left.height if node.left != None else 0)
        return new_node
    
    def balanced_inserting(self, key):
        # get added node
        x = self.insert_key(key)
        self._balance(x)         
    
    def _balance(self, x):
        y = x.parent
        if y == None:
            return

        z = y.parent
        if z == None:
            return

        # travers tree from there to find unbalanced node
        while z != None:
            balance_factor = self.get_height(z.right) - self.get_height(z.left)
            
            # check unbalancement conditions
            if balance_factor > 1 or balance_factor < -1:
                case = self._get_unbalancement_case(x,y,z)
                if case == UnbalancementCase.LEFT_LEFT:
                    self._right_rotate(z)
                if case == UnbalancementCase.LEFT_RIGHT:
                    self._left_rotate(y)
                    self._right_rotate(z)
                if case == UnbalancementCase.RIGHT_LEFT:
                    self._right_rotate(y)
                    self._left_rotate(z)
                if case == UnbalancementCase.RIGHT_RIGHT:
                    self._left_rotate(z)
                
                self._update_heights()
                return
            
            z, y, x = z.parent, z, y
    
    def _update_heights(self):
        my_root = self.root
        my_root.height = 1 + max(self._update_heights_internal(my_root.right), self._update_heights_internal(my_root.left))
    
    def _update_heights_internal(self, node):
        if node == None:
            return -1
        else:
            node.height = 1 + max(self._update_heights_internal(node.right), self._update_heights_internal(node.left))
            return node.height 



    def _right_rotate(self, z):
        y = z.left
        t3 = y.right
        # change the child of the parent of z to become y
        if z.parent != None:
            if z.parent.right == z:
                z.parent.right = y
            else:
                z.parent.left = y


        # put y in the place of z
        y.parent = z.parent
        y.right = z
        z.parent = y

        # move t3 to the left of z
        z.left = t3
        
        if t3 != None:
            t3.parent = z
        
        # case where z is the root node 
        if y.parent == None:
            self.root = y

    def _left_rotate(self, z):
        y = z.right
        t2 = y.left
        # changing the child of z parent to y
        if z.parent != None:
            if z.parent.right == z:
                z.parent.right = y
            else:
                z.parent.left = y

        # Put y as parent of z and z on the left of y
        y.parent = z.parent        
        z.parent = y
        y.left = z

        # Put t2 on the right of z
        z.right = t2
        if t2 != None:
            t2.parent = z

        # in case z was the root, it should change to y
        if y.parent == None:
            self.root = y


    # Update height of nodes after 
    def _get_unbalancement_case(self, x, y, z):
        case = UnbalancementCase.LEFT_LEFT
        if z.right == y and y.right == x:
            case = UnbalancementCase.RIGHT_RIGHT
        if z.right == y and y.left == x:
            case = UnbalancementCase.RIGHT_LEFT
        if z.left == y and y.right == x:
            case = UnbalancementCase.LEFT_RIGHT
        return case

    def get_height(self, node):
        return node.height if node != None else -1 


    def get_coord_dict(self):
        if self.root == None:
            print('u passed an empty tree')
        tree_depth = self.depth
        coord_dict = {k: [] for k in range(1, tree_depth + 2)}
        # remplir le niveau n d'abord
        mov_unity = (width - 2*w_margin)/(2**(tree_depth) - 1)
        last_level_x_coord = list(np.arange(w_margin, width - w_margin + 1, mov_unity))

        coord_dict[tree_depth + 1] = last_level_x_coord
        
        i = tree_depth
        while i > 0:
            for j in range(0, len(coord_dict[i+1]) - 1, 2):
                coord_dict[i].append((coord_dict[i+1][j] + coord_dict[i+1][j + 1])/2)
            i -= 1
        return coord_dict


    
    def draw(self):

        print('*'*10 + 'TREE DRAWING' + '*'*10)
        
        # adding drawing coordinates to nodes 
        self.insert_coords()
        screen.fill(white)
        
        # case of empty tree
        if self.root == None:

            font = pygame.font.SysFont('verdana', 10)
            text = font.render('You loaded an empty tree', True, black)
            text_rect = text.get_rect()
            text_rect.center = (width/2, height/2)
            screen.blit(text, text_rect)    

            display()
        
        else:
            tree_depth = self.depth
            # unit of movement in the y direction
            global y_mov_unit
            y_mov_unit = (height - 2*h_margin)/(tree_depth)

            global coords_dict 
            coords_dict = self.get_coord_dict()

            self.draw_internal(self.root, screen)
            display()
    
    def draw_internal(self, node, screen):
        if node == None:
            return
        else:            
            node.draw(screen)
            node.draw_branches(screen)        
            self.draw_internal(node.left, screen)
            self.draw_internal(node.right, screen)
            return    


    
    def insert_coords(self):
        print('*'*10 + 'INSERT COORDS' + '*'*10)
        # check if the tree is empty
        if self.root == None:
            return
        
        self.root.coords = [1, 0]
        self.__insert_coords(self.root.left)
        self.__insert_coords(self.root.right)
        return
    
    def __insert_coords(self, node):
        if node == None:
            return
        else:
                parent_node = node.parent
                if node == parent_node.left:
                    node.coords = [parent_node.coords[0] + 1, 2*parent_node.coords[1]]
                else:
                    node.coords = [parent_node.coords[0] + 1, 2*parent_node.coords[1] + 1]
        
        self.__insert_coords(node.left)
        self.__insert_coords(node.right)
        return
        

    def search(self, key):
        if self.root == None:
            return 
        else:
            if self.root.key == key:
                return self.root
            else:
                if key > self.root.key:
                    return self.__intern_search(self.root.right, key)
                else:
                    return self.__intern_search(self.root.left, key)
                    

    def __intern_search(self, node, key):
        if node == None:
            return False
        else:
            if key == node.key:
                return node
            else:
                if key > node.key:
                    return self.__intern_search(node.right, key)
                else:
                    return self.__intern_search(node.left, key)


def normal_search(listos, elet):
    
    for item in listos:
        if item == elet:
            return True
    return False

def time_it(func, *args):
    start = time.time()
    func(*args)
    end = time.time()
    return end - start

def main():
    # list to be converted to tree
    listos = list(range(1,11))

    # tree holding the list
    balanced_tree = Tree()

    # add elements to the tree
    for i in listos:
        balanced_tree.balanced_inserting(i)
    
    #initialising drawing parameters with pygame 
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    
    # drawing the tree
    balanced_tree.draw()
    
    #print(time_it(normal_search, listos, 500))
    #print(time_it(balanced_tree.search, 500))


if __name__ == '__main__':
    main()