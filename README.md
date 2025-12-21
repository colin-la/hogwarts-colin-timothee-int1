# Hogwarts-colin-timothee-int1
    
### Description
    This project is a textual game that takes place in the hogwarts legacy world.   
    You will have to make choices
    that will influence your experience and adventure.
    Good luck and have fun !

### Contributors 
   >[Colin](https://github.com/colin-la/ "@colin-la")   
   >[Timothee](https://github.com/Tim-syr/ "@Tim-syr")


### Installation
> [!WARNING]  
> Before installing our game, you need to have python AND git installed on your machine.   
>   
> If you install it on your own (without the command), be sure to launch the main.py in the hogwarts-colin-timothee-int1 folder (due to error with relative file path with "../")

> [!TIP]   
> Here is the link to the [Python Website](https://www.python.org/downloads/ "https://www.python.org/downloads/")    
> And here is the link to the [Git Website](https://git-scm.com/install/windows "https://git-scm.com/install/windows") 
```
1. Open your terminal window    
Win+R -> Type cmd -> Press Enter 
```


```
2. Copy/Paste the following command to install the game (in the Documents folder):
```
<details>
    <summary>Installation Command</summary>
<p>
cd %userprofile%/Documents && git init && git clone git@github.com:colin-la/hogwarts-colin-timothee-int1.git && rmdir /s /q .git
</p>
</details>



### Usage
    If you want to launch the game, launch this command (in your terminal of course):
    
<details>
    <summary>Launch Command</summary>
<p>
cd %userprofile%/Documents/hogwarts-colin-timothee-int1 && python main.py
</p>
</details>

### Key Features

- A story game where your choice really matters
- Mini game to learn spells
- Mini game to earn points for your house
- And of course, much more ! 


# Log Book
### Project Timeline

<details>
<summary>27 and 28 November 2025</summary>
<p> 
    - Beggining of the project <br>
    - Creation of folder tree with all files <br>
    - Create branch_test to learn git
</p>
</details>

<details>
<summary>3 December 2025</summary>
<p> 
    - Finished input_utils.py <br>
    - Started Chapter1
</p>
</details>


<details>
<summary>5 December 2025</summary>
<p> 
    - create_character() and ask_number() functions fix because of wrong return value <br>   
    - Added .gitignore to avoid pushing __pycache__ and .idea folder
</p>
</details>


<details>
<summary>10 December 2025</summary>
<p> 
- Finished Chapter1.py <br>
- Finished houses.py
</p>
</details>


<details>
<summary>12 December 2025</summary>
<p>    
- Little fix on a while loop in main.py   <br>
- Fixed a problem in the launch_menu() function that didn't return the dictionnary as expected.
</p>
</details>

<details>
<summary>19 December 2025</summary>
<p>    
- Finished Chapter2.py <br>
- Finished Chapter3.py<br>   
- Test on all chapters: no bug !<br>
- Init Chapter4.py (Quidditch match)<br>
- Fix path problem due to "../data/" because if we 
launchs from the main.py, we are not in the same 
folder then, we needed to remove "../" and just
put "./" (no need to go up in the folder tree)
</p>
</details>

### Task Distribution

      
##### [Colin](https://github.com/colin-la/ "@colin-la") worked on:

> [input_utils.py](https://github.com/colin-la/hogwarts-colin-timothee-int1/blob/main/utils/input_utils.py "input_utils.py")   
> [menu.py](https://github.com/colin-la/hogwarts-colin-timothee-int1/blob/main/menu.py "menu.py")   
> [chapter1.py](https://github.com/colin-la/hogwarts-colin-timothee-int1/blob/main/chapter/chapter1.py "chapter1.py")   
> [chapter2.py](https://github.com/colin-la/hogwarts-colin-timothee-int1/blob/main/chapter/chapter2.py "chapter2.py")   

##### [Timothee](https://github.com/Tim-syr/ "@Tim-syr") worked on:

> [house.py](https://github.com/colin-la/hogwarts-colin-timothee-int1/blob/main/universe/house.py "house.py")   
> [character.py](https://github.com/colin-la/hogwarts-colin-timothee-int1/blob/main/universe/character.py "character.py")   
> [main.py](https://github.com/colin-la/hogwarts-colin-timothee-int1/blob/main/main.py "main.py")   
> [chapter3.py](https://github.com/colin-la/hogwarts-colin-timothee-int1/blob/main/chapter/chapter3.py "chapter3.py")

# Control, Testing, and Validation
### Input and Error Management
    In the ask_choice, ask_number and ask_text functions, we used try / exept statements (which was explicitly authorized by our professor) to handle input errors

    
### Testing Strategies
    We used this statement to test each functions in each files individually and regularly
```python    
if __name__ == "__main__":
    # test of the functions
```

    If functions needed input from the user, we entered anything (numbers when we needed letters and vice-versa).
    No major bugs were seen. 