# import node class 
from project_node import ProjectNode

# import tree class 
from project_tree import ProjectTree

def main():
    """
    The function that runs the program.
    :return: None
    """
    ############################YOUR CODE GOES HERE#####################################
    # 1. Build two trees -- one will store the possible_words and the other will store the correct answers.

    # Building two trees - one for each txt file 
    correct_tree = ProjectTree()
    possible_tree = ProjectTree()

    # Loading txt file into trees with build_project_tree function 
    correct_tree.build_project_tree("correct_answers.txt") 
    possible_tree.build_project_tree("possible_words.txt")

    # 2. Traverse both trees - store the results AND output how many elements belong to each list

    correct_list = []
    #get root node from correct_tree 
    root = correct_tree.get_root()
    #call traversal function 
    correct_tree.traversal(root, correct_list)

    possible_list = []
    # get root node from possible_tree
    root = possible_tree.get_root()
    # call traversal function 
    possible_tree.traversal(root, possible_list)

    # 3. Allow the user to input a prefix that they would like to search both trees for.

    prefix = input("What prefix are you looking for?:")

    # Searching both trees for words with the inputted prefix 
    correct_words = correct_tree.word_starts_with(prefix)
    possible_words = possible_tree.word_starts_with(prefix)

    # 4. Print the results of both searches -- make sure to add context to make it clear which results are from which
    #    tree

    print("Words starting in",prefix,"from Correct Answers: ",correct_words)
    print("Words starting in",prefix,"from Possible Words: " ,possible_words)

    # 5. Using word_starts_with, print all of the words that start with 'ha' from each list

    print("Words starting in 'ha' from Correct Answers",correct_tree.word_starts_with('ha'))
    print("Words starting in 'ha' from Possible Words",possible_tree.word_starts_with('ha'))

    # 6. Remove all of the correct answers from the possible words tree
    #    (i.e., The possible words tree should now just hold incorrect answers.)

    # Loop through correct_list and delete every word that is in the possible_tree
    for word in correct_list:
        possible_tree.delete(root, word, 0)

    # 7. Using word_starts_with, print both the possible correct answers that begin with 'ha' and the words that
    #    begin with 'ha' that CANNOT be correct answers.

    print("Words starting in 'ha' that are correct answers",correct_tree.word_starts_with('ha'))
    print("Words starting in 'ha' that cannot be correct answers",possible_tree.word_starts_with('ha'))

    return None 

main()

