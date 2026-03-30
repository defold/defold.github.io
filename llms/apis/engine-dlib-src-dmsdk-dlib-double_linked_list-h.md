# Double linked list structs and functions

**Namespace:** `dmDoubleLinkedList`
**Language:** C++
**Type:** Defold C++
**File:** `double_linked_list.h`
**Source:** `engine/dlib/src/dmsdk/dlib/double_linked_list.h`
**Include:** `dmsdk/dlib/double_linked_list.h`

Double linked list structs and functions

## API

### dmDoubleLinkedList::ListAdd
*Type:* FUNCTION
Added new list element as a head of the list

**Parameters**

- `list` (dmDoubleLinkedList::List*) - the list
- `item` (dmDoubleLinkedList::ListNode*) - new list element

### dmDoubleLinkedList::ListGetFirst
*Type:* FUNCTION
Get the first element of the list. If the list is empty (tail == head) returns 0.

**Parameters**

- `list` (dmDoubleLinkedList::List*) - the list

**Returns**

- `first_element` (dmDoubleLinkedList::ListNode*) - the first element of the list.  If the list is empty (tail == head) returns 0

### dmDoubleLinkedList::ListGetLast
*Type:* FUNCTION
Get the last element of the list. If the list is empty (tail == head) returns 0.

**Parameters**

- `list` (dmDoubleLinkedList::List*) - the list

**Returns**

- `last_element` (dmDoubleLinkedList::ListNode*) - the last element of the list. If the list is empty (tail == head) returns 0

### dmDoubleLinkedList::ListInit
*Type:* FUNCTION
Initialize empty double linked list

**Parameters**

- `list` (dmDoubleLinkedList::List*) - the list

### dmDoubleLinkedList::ListRemove
*Type:* FUNCTION
Remove item from the list. Doesn't deallocate memory allocated for the item.
If element is not in the list function doesn't affect linked list.

**Parameters**

- `list` (dmDoubleLinkedList::List*) - the list
- `item` (dmDoubleLinkedList::ListNode*) - removed item
