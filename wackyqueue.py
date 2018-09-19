"""
# Copyright Nick Cheng, 2018
# Copyright Rashida Kapadia, 2018
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSCA48, Winter 2018
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""

from wackynode import WackyNode

# Do not add import statements or change the one above.
# Write your WackyQueue class code below.


class WackyQueue():
    ''' Represents a Wacky Queue class '''
    def __init__(self):
        ''' (WackyQueue) -> NoneType
        Initialize the references of an empty Wacky Queue
        '''
        # representation invariant
        # self._odd_head is the pointer to every other node in wacky queue,
        # starting from the first node
        # if self._odd_head = None:
        #  wacky queue is empty
        # else:
        #  self._odd_head = WackyQueue
        # Farther the nodes from self._odd_head, lower the priority
        # self._even_head is the pointer to every other node in WackyQueue,
        # starting from the second node
        # if self._even_head = None:
        #  WackyQueue is empty or contains only one node
        # else:
        #  self._even_head = WackyQueue
        # Farther the nodes from self._even_head, lower the priority

        # Initialize the heads pointing to the 2 linked lists - odd and even
        self._odd_head = None
        self._even_head = None

""" ANNOTATION 2: Method should be less than 73 lines """
    def insert(self, item, priority):
""" END ANNOTATION 2 """
        ''' (WackyQueue, obj, int) -> NoneType
""" ANNOTATION 1: How do the priorities work? """
        Insert an item with a priority into the Wacky Queue.
        Duplicates are allowed - wacky queue may contain same copies of obj
        with same or different priorities.
""" END ANNOTATION 1 """
        '''
        # Create a new node that will be inserted into the wacky queue
        new_node = WackyNode(item, priority)

        # If the WackyQueue is empty, add the new node to the first position of
        # WackyQueue (first position of odd linked list)
        if self._odd_head is None:
            self._odd_head = new_node
        # If the WackyQueue contains only one node and if the new node has a
        # priority greater than the first node,
        elif ((self._even_head is None) and (new_node.get_priority() >
                                             self._odd_head.get_priority())):
            # Switch the first node to the second node's position and insert
            # new node to first node's position
            self._even_head = self._odd_head
            self._odd_head = new_node
        # If the WackyQueue contains only one node and if the priority of new
        # node is lesser than that of first node,
        elif self._even_head is None:
            # Add the new node to the second position of WackyQueue
            # (ie. 1st position of even linked list)
            self._even_head = new_node
        # Else, loop through both linked lists till we find a priority lesser
        # than the priority of new node
        else:
            # Set temporary variables to represent the nodes in the linked list
            # while traversing through the linked list
            odd_curr = self._odd_head
            even_curr = self._even_head
            odd_prev = None
            even_prev = None
            while ((odd_curr is not None) and (even_curr is not None) and
                    (odd_curr.get_priority() >= new_node.get_priority()) and
                    (even_curr.get_priority() >= new_node.get_priority())):
                odd_prev = odd_curr
                even_prev = even_curr
                odd_curr = odd_curr.get_next()
                even_curr = even_curr.get_next()
            # If we need to insert in between the positions of the first two
            # nodes of the WackyQueue
            if (odd_prev is None) or (even_prev is None):
                # If we need to insert new node before the first node of queue
                if odd_curr.get_priority() < new_node.get_priority():
                    # Set the even head pointer to the first node and then add
                    # the new node at the first position
                    self._even_head = self._odd_head
                    self._odd_head = new_node
                    # Switch the nodes to their correct positions
                    new_node.set_next(even_curr)
                # If we need to insert the new node before the second node of
                # the WackyQueue
                elif even_curr.get_priority() < new_node.get_priority():
                    self._even_head = new_node
                    new_node.set_next(odd_curr.get_next())
                    odd_curr.set_next(even_curr)

            # Given that there are atleast two WackyNodes in WackyQueue
            # If we need to insert at the end of the odd linked list
            elif odd_curr is None:
                odd_prev.set_next(new_node)
            # If we need to insert at the end of the even linked list
            elif ((even_curr is None) and
                  (odd_curr.get_priority() >= new_node.get_priority())):
                even_prev.set_next(new_node)
            # If we need to insert at the end of the odd linked list,
            # where there is already a node present whose priority is less
            # than that od new node
            elif even_curr is None:
                even_prev.set_next(odd_prev.get_next())
                odd_prev.set_next(new_node)

            # If we need to insert in between the nodes of an odd linked list
            elif odd_curr.get_priority() < new_node.get_priority():
                # Set the new node in the same position as the odd node with
                # lesser priority and adjust the positions of the subsequent
                # nodes according to their new positions.
                # Odd nodes go the even linked list and even nodes go to odd ll
                odd_prev.set_next(new_node)
                new_node.set_next(even_curr)
                even_prev.set_next(odd_curr)
            # If we need to insert in between the nodes of an even linked list
            elif even_curr.get_priority() < new_node.get_priority():
                # Set the new node in the same position as the even node with
                # lesser priority and adjust the positions of the subsequent
                # nodes according to their new positions.
                # Odd nodes go the even linked list and even nodes go to odd ll
                even_prev.set_next(new_node)
                new_node.set_next(odd_curr.get_next())
                odd_curr.set_next(even_curr)

    def extracthigh(self):
        ''' (WackyQueue) -> obj
        Removes and returns the first item in the wacky queue
        REQ: WackyQueue is not empty
        '''
        # Find the item in the wacky queue with highest priority
        # This item will be the node at which head of the odd list points to

        # Create a temporary variable to store the node and item of the node
        # before removing from linked list
        temp = self._odd_head
        temp_item = self._odd_head.get_item()
        # Make the pointer of head point to the next node
        self._odd_head = self._odd_head.get_next()
        # Set the pointer of the removed node to None
        temp.set_next(None)
        # Switch the head of odd list to point to even linked list and
        # Switch the head of even linked list to point to odd linked list
        # This is to update the linked lists so that the obj of highest
        # priority is in the first node of the odd linked list
        self._odd_head, self._even_head = self._even_head, self._odd_head
        # Return the object of the highest priority node that was extracted
        return temp_item

    def isempty(self):
        '''(WackyQueue) -> bool
        Returns true iff the wacky queue is empty
        '''
        # For wacky queue to be empty, the head of odd linked list should
        # point to None since it represents the very first node of the queue
        return (self._odd_head is None)

    def changepriority(self, item, priority):
        ''' (WackyQueue, obj, int) -> NoneType
        Change the first copy of a given obj to a new priority.
        If obj with same pri is already in the list, or, obj is not in list,
        list is unchanged.
        '''
        # Loop through the two linked lists until you reach the node with
        # the same obj or pri as the given input
        odd_curr = self._odd_head
        even_curr = self._even_head
        odd_prev = None
        even_prev = None
        while ((odd_curr is not None) and (even_curr is not None) and
               (odd_curr.get_item() is not item) and
               (even_curr.get_item() is not item)):
            odd_prev = odd_curr
            even_prev = even_curr
            odd_curr = odd_curr.get_next()
            even_curr = even_curr.get_next()
        # If we reach the end of the linked lists and if the lists are of
        # unequal size
        if (even_curr is None) and (odd_curr is not None):
            # If the last node in odd linked list contais the obj, with diff
            # priority,
            if ((odd_curr.get_item() is item) and
               (odd_curr.get_priority() is not priority)):
                # We need to first delete the node from the linked list and
                # then insert it in again with the new priority
                # If there are less than 3 nodes
                if odd_prev is None:
                    self._odd_head = None
                # If there are more than 3 nodes
                else:
                    odd_prev.set_next(None)
                self.insert(item, priority)
            # Do nothing if the object is found, but contains the same priority
            # as the new given priority
            else:
                pass
        # Also do nothing if object is not found and we have reached the end.
        # This code ensures that we do not enter the other cases and so
        # we allow our program to enter and pass from this case
        elif odd_curr is None:
            pass

        # If we find the node with object with diff priority in the beginning
        # or middle of odd linked list
        elif ((odd_curr.get_item() is item) and
              (odd_curr.get_priority() is not priority)):
            # If we need to insert at the beginning of WackyQueue
            # More than two nodes
            if odd_prev is None and odd_curr.get_next() is not None:
                self._even_head = odd_curr.get_next()
                self._odd_head = even_curr
            # Less than or equal to two nodes
            elif odd_prev is None:
                self._odd_head = even_curr
                self._even_head = None
            # If we need to insert in the middle of an odd linked list of
            # WackyNodes
            else:
                # First delete the item from the linked list
                odd_prev.set_next(even_curr)
                even_prev.set_next(odd_curr.get_next())
            # Insert the node with updated priority by calling insert method
            self.insert(item, priority)
        # If we find the node with object with diff priority in the beginning
        # or middle of even linked list
        elif ((even_curr.get_item() is item) and
              (even_curr.get_priority() is not priority)):
            # If we need to insert at the beginning of WackyQueue
            # More than two nodes
            if even_prev is None and even_curr.get_next() is not None:
                self._even_head = odd_curr.get_next()
                odd_curr.set_next(even_curr.get_next())
            # Less than or equal to two nodes
            elif even_prev is None:
                self._even_head = odd_curr.get_next()
            # If we need to insert in the middle of an even linked list of
            # WackyNodes
            else:
                # First delete the item from the linked list
                odd_curr.set_next(even_curr.get_next())
                even_prev.set_next(odd_curr.get_next())
            # Insert the node with updated priority by calling insert method
            self.insert(item, priority)

    def negateall(self):
        ''' (WackyQueue) -> NoneType
        Negates all the priorities in the wacky queue
        '''
        # Reverse the order of both linked lists by traversing through the
        # linked list
        odd_prev = None
        even_prev = None
        odd_curr = self._odd_head
        even_curr = self._even_head
        # Assume that the size of both linked lists are initially equal
        size_equal = True
        while (odd_curr is not None):
            # Multiply all the priorities of the nodes by -1
            odd_curr.set_priority(odd_curr.get_priority()*(-1))
            # Reverse the pointers till we get to the end of the list
            odd_temp = odd_curr.get_next()
            odd_curr.set_next(odd_prev)
            odd_prev = odd_curr
            odd_curr = odd_temp
            # If the size of odd and even linked lists are unequal, continue
            # reversing the even linked list
            if even_curr is not None:
                even_curr.set_priority(even_curr.get_priority()*(-1))
                even_temp = even_curr.get_next()
                even_curr.set_next(even_prev)
                even_prev = even_curr
                even_curr = even_temp
            # If the size of both linked lists are not equal,
            else:
                # Since both linked lists are unequal in size,
                # do not switch them. Just set the heads to point to the prevs
                self._odd_head = odd_prev
                self._even_head = even_prev
                # Set the size to be unequal
                size_equal = False

        # Switch the pointers of odd and even linked lists since the sizes
        # of both lists are of equal length
        if size_equal is True:
            self._odd_head = even_prev
            self._even_head = odd_prev

    def getoddlist(self):
        ''' (WackyQueue) -> WackyNode
        Returns a pointer to the linked list contanining every other object in
        the queue, starting fromt the first object
        '''
        # If their is no first obj, then an empty list is returned (None)
        return self._odd_head

    def getevenlist(self):
        ''' (WackyQueue) -> WackyNode
        Returns a pointer to the linked list contanining every other object in
        the queue, starting fromt the first object
        '''
        # If there is no second obj, then an empty list is returned(None)
        return self._even_head
