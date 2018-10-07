#methods.py
# Create the following methods and make sure they return the correct data type and/or value
# - num_list_with_arg, it should take one argument that is an integer, assume that integer is a positive number above 1. it should return a list of integers from 1 to the argument that is provided to the method
# - has_ruby_exp, this method is already created but needs modifications. it should 
#     - in the method create a list called ruby_experience
#     - iterate through the dictionary experience and add the name of the teachers that have ruby experience to the ruby_experience list
#     - then sort the list
#     - return the list
# - toggle_str_num, this method should be provided an arugment
#     - if the arugment is a string, change it to a number and return it
#     - if ithe argument is an integer, change it to a string and return iter
#     - if it is neither return "this is not a str or a int"



def has_ruby_exp():
    experience = {
        'jimmy': {
            'bjj': False,
            'soccer': False,
            'ruby': True,
            'baking': True,
            'biking': True,
            'pasta': False
        },
        'don': {
            'bjj': False,
            'soccer': False,
            'ruby': True,
            'baking': True,
            'biking': False,
            'pasta': False
        },
        'zakk': {
            'bjj': False,
            'soccer': False,
            'ruby': True,
            'baking': False,
            'biking': False,
            'pasta': True
        },
        'hector': {
            'bjj': True,
            'soccer': True,
            'ruby': False,
            'baking': False,
            'biking': True,
            'pasta': False
        }
    }