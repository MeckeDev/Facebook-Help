""" This Module generates Patterns depending on the User Input """


def create_tile(size):
    """
    Creates a Tile Pattern of a given Size

                    EXAMPLE
                        *
                      * * *
                    * * * * *
                      * * *
                        *
    """

    text = "\n".join([f'{"* " * x}'.center(size * 2) for x in range(1, size + 1)]) + "\n"
    text += "\n".join([f'{"* " * x}'.center(size * 2) for x in range(size-1, 0, -1)])

    print(text)


def create_cross(size):
    """ Creates a Cross Pattern of a given Size

                    EXAMPLE
                    * * * * *
                      * * *
                        *
                      * * *
                    * * * * *
    """

    text = "\n".join([f'{"* " * x}'.center(size * 2) for x in range(size, 0, -1)]) + "\n"
    text += "\n".join([f'{"* " * x}'.center(size * 2) for x in range(2, size + 1)])

    print(text)


task = input(f"""
Create a Pattern 
Enter T or X followed by the Size

Example T3
{create_tile(3)}

Example X3
{create_cross(3)}

Your Input: """)

if task.lower().startswith("x"):
    create_cross(int(task[1:]))
elif task.lower().startswith("t"):
    create_tile(int(task[1:]))
