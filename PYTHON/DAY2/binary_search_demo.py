import sys
import binay_search

print(f'The Input numbers are\n' ,{sys.argv[1:-1]})
print(f'The search element is {sys.argv[-1]}')

search_element_index = binay_search(sys.argv[1:-1],sys.argv[-1])

if search_element_index == -1:
    print(f'The search ')
