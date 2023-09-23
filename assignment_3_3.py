#!/usr/bin/env python
# coding: utf-8

# In[1]:


# MSDS 532 (DATA SCIENCE PROGRAMING WITH PYTHON-FALL 2023 1ST BI-TERM)
# WEEK 4 ASSIGNMENT- PROBLEM SET 3- TASK 3
# TITLE: PROVIDING NEAREST FEASIBLE ALTERNATIVE COMBINATION OF CHICKEN NUGGETS
# DATE: FRIDAY, SEPTEMBER 22, 2023
# STUDENT/AUTHOR: STEPHEN SARPONG LARTEY
# STUDENT ID: 005015848
# COURSE INSTRUCTOR: DR. ARNETT CAMPBELL


# In[2]:


def is_feasible_quantity(quantity, box_sizes):
    # Recursive function to check if a quantity is feasible using available box sizes
    if quantity == 0:
        return True
    if quantity < 0:
        return False
    
    # Try each box size to see if it leads to a feasible quantity
    for box_size in box_sizes:
        if is_feasible_quantity(quantity - box_size, box_sizes):
            return True
    
    return False


# In[3]:


def find_lowest_cost_option(quantity):
    # Define the available box sizes and their respective costs
    box_sizes = [6, 9, 22]
    costs = [3, 4, 9]  # Costs associated with 6-piece, 9-piece, and 22-piece options
    
    # Initialize variables for the lowest cost option
    lowest_cost = float('inf')  # Initialize with positive infinity
    lowest_option = None
    
    # Iterate through possible quantities of each box size
    for six_count in range(quantity // 6 + 1):
        for nine_count in range(quantity // 9 + 1):
            for twenty_two_count in range(quantity // 22 + 1):
                # Calculate the total number of nuggets for the current combination
                total_nuggets = 6 * six_count + 9 * nine_count + 22 * twenty_two_count
                
                # Check if the total matches the requested quantity
                if total_nuggets == quantity:
                    # Calculate the cost for the current combination
                    total_cost = 3 * six_count + 4 * nine_count + 9 * twenty_two_count
                    # Check if the current combination has a lower cost
                    if total_cost < lowest_cost:
                        lowest_cost = total_cost
                        lowest_option = {
                            'Six_piece': six_count,
                            'Nine_piece': nine_count,
                            'Twenty_two_piece': twenty_two_count
                        }
    
    return lowest_option, lowest_cost


# In[4]:


def find_nearest_feasible_quantity(quantity):
    # Define the available box sizes
    box_sizes = [6, 9, 22]
    
    # Initialize the nearest feasible quantity to None
    nearest_feasible_quantity = None
    
    # Iterate from the requested quantity down to 0
    for i in range(quantity, -1, -1):
        # Check if the current quantity is feasible using available box sizes
        if is_feasible_quantity(i, box_sizes):
            nearest_feasible_quantity = i
            break  # Stop iterating when the nearest feasible quantity is found
    
    return nearest_feasible_quantity


# In[9]:


def main():
    # Get the quantity of chicken nuggets requested by the user
    quantity = int(input("How many chicken nuggets would you like to order? "))
    
    # Find the lowest cost option and cost
    lowest_option, lowest_cost = find_lowest_cost_option(quantity)
    
    if lowest_option is not None:
        print(f"For an order size of {quantity}, the lowest cost option is:")
        print(lowest_option)
        print(f"Total Cost: ${lowest_cost}")
    else:
        # If no feasible quantity is found, suggest a different quantity
        nearest_feasible_quantity = find_nearest_feasible_quantity(quantity)
        if nearest_feasible_quantity is not None:
            print(f"Sorry, your requested quantity is not feasible. Consider ordering {nearest_feasible_quantity} nuggets.")
            print(f"For an order size of {nearest_feasible_quantity}, the lowest cost option is:")
            nearest_option, nearest_cost = find_lowest_cost_option(nearest_feasible_quantity)
            print(nearest_option)
            print(f"Total Cost: ${nearest_cost}")
        else:
            # If no feasible quantity is found, inform the user
            print(f"Sorry, there are no feasible order quantities with the available box sizes.")

if __name__ == "__main__":
    main()


# In[ ]:




