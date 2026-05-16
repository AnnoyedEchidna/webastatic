"""
Main! You should know what main is.
"""

from markdownmodules import markdown_to_html_node


def main():
    """
    main.py definition
    """
    dummy_text_node = markdown_to_html_node(
        """ # Lost on the Interwebs

Oh **look**! We have found a link!
I wonder where it goes...
[Here is some anchor text](https://localhost:8000)

## In a weird place never before seen

_Somewhere between webpages on localhost_ Where are we? This doesn't feel like the **internet**.
What are you talking about? You have to review the field manual.

> To access previously visited webpages, please click the back button on your mouse.
If this has no affect, consider the following:

- Ctrl+W
- Alt+F4
- Pressing the power button on the front of your computer

1. Restarting the system
2. Try entering a command with sudo
3. Finding inner peace and remaining where you are until rescue arrives

```
Press(Ctrl+W)
rerun
```

#### Back on the desktop

_Back upon a hill somewhere much like this:_
![grassy knoll with wildflowers](src/link/to/hill.png)
_Our adventurers find themselves confused but relieved_
I'm so glad we're back on this hill! It's been too long on the internet
"""
    ).to_html()
    print(dummy_text_node)


if __name__ == "__main__":
    main()
