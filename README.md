# Do Bot Bar
## Personal Task and list Manager
Personal bot to improve efficiency and work automation<br>

# Table of Contents

- [Dictionery](#dictionery)
  <!-- * [Sub-heading](#sub-heading) -->
    <!-- + [Sub-heading](#sub-heading) -->
- [Orders](#orders)
- [Content](#content)
- [Roadmap](#roadmap)
- [Note](#note)

<!-- toc -->

## Dictionery
All of terms used in writing this program.

* `[user]` - Anyone who enters the content, person. 
* `[order]` - The functions we want to call, order ( to do some thing ) we want to give, the order is given first.
* `[content]` - This is the content of the order, most orders require content. The **[content]** is given after **[order]**.
* `[#]`- a special character that allows us to recognize **[order]** from the rest of user input date

## Orders
that is, the commands that can be given by the user
All `orders` should have a special character prefix `#` 
for example: <br>
`#add`, `#del`, `#show` and so on

- `add` - add new content to the list
- `del` - remove existing content from the list
- `show` - show/display from the list

## Content
Any content ( information, position ) that the user wants to add to the list, content can by added and content can by removd from the list. There is no history at this moment. And the content is saved in simple JSON files. There is only one list at the moment.

## Roadmap
+ **basic_interpreter** - add veriable to take list of orders
    + clean up code
    + clean up description
    + setup more test for the function
+ rebuild main file
    + set up test for main loop
+ list of orders in JSON file
    + load list from JSON


## Note

### Note 01 
Old loop to be store for a while

``` python
while True:
    user_function = input('Wybierz fuinkcje: ')
    if user_function in f_list:
        user_input = input('podaj dane: ')
        user_function = locals()[user_function]
        user_function(user_input)
    elif user_function in u_list:
        user_function = locals()[user_function]
        user_function()
    else:
        print('nie ma takiej funkcji ani operacji' , end='\n')
```