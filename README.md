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
> Before installing our game, you need to have python installed on your machine.

> [!TIP]   
> Here is the link to the python website:   
>[Python Website](https://www.python.org/downloads/ "https://www.python.org/downloads/") 

```
1. Open your terminal window    
Win+R -> Type cmd -> Press Enter 
```


```
2. Copy/Paste the following command to install the game (in the Documents folder):
```
<details>
    <summary>Command</summary>
<p>
cd %userprofile%/Documents && git init && git clone git@github.com:colin-la/hogwarts-colin-timothee-int1.git && rmdir /s /q .git
</p>
</details>



### Usage
    If you want to launch the game, launch this command (in your terminal of course):
    
<details>
    <summary>Command</summary>
<p>
python %userprofile%/Documents/hogwarts-colin-timothee-int1/main.py
</p>
</details>

### Key Features
    List of key features


# Log Book
### Project Timeline
    Dates and descriptions of key milestones, decisions made, and
    problems encountered.

### Task Distribution
    Colin worked on:
        input_utils.py
        menu.py
        chapter1.py
        chapter2.py

    Timothee worked on:
        house.py
        character.py
        main.py
        chapter3.py

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