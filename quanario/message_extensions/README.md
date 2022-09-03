# [Documentation](../) / Message_extensions


### [carousel.py](carousel.py)
><details><summary>Class `Carousel` - The main class for creating attachments of the `Carousel` type. The difference between the carousel and ordinary messages is its unusual appearance, the carousel consists of blocks (maximum 10 pcs.), each block has a title, description and picture. Subsequently, it is possible to attach to each block unique keyboard. It is important that the number of buttons matches in all blocks!!!</summary><p>
>
>* `count`: [int](#carouselpy) - This _Property_ contains the number of elements in the carousel.
>* `last_element`: [CarouselElement](#carouselpy) - This _Property_ contains the `last element` added to the `carousel`, thereby opening the possibility of its editing, for example, to change the description or change the photo.
>* `add_element()`: [None](#carouselpy) - This method `creates a new block` for the `carousel` and adds it to the existing ones.
>* `get_carousel()`: [json](#carouselpy) - This method `builds` the entire `carousel`, for later sending it to the user.
>
></p></details>

><details><summary>Class `CarouselElement` - A class representing a single `carousel' element.</summary><p>
>
>* `title`: [str](#carouselpy) - This _Property_ contains the block header.
>* `title`: [None](#carouselpy) - The `setter` for the `title` _Property_ allows you to set a new value for the _Property_.
>* `description`: [str](#carouselpy) - This _Property_ contains the block description.
>* `description`: [None](#carouselpy) - The `setter` for the `description` _Property_ allows you to set a new value for the _Property_.
>* `attachment`: [str](#carouselpy) - This _Property_ contains a link to the block image.
>* `attachment`: [None](#carouselpy) - The `setter` for the `attachment` _Property_ allows you to set a new value for the _Property_.
>* `keyboard`: [json](#carouselpy) - This _Property_ contains json with buttons for the element.
>* `keyboard`: [None](#carouselpy) - The `setter` for the `keyboard` _Property_ allows you to set a new value for the _Property_.
>* `compile()`: [Dict](#carouselpy)[[str](#carouselpy), [Any](#carouselpy)] - This method performs the `assembly` of the carousel block, for subsequent sending it to the user.
>* *`__check_length()`: [str](#carouselpy) - This `privat` method shortens the input string to the specified `count` length.*
>* *`__cut_attachment()`: [str](#carouselpy) - This `private` method allocates a unique image id from the input `attachment`*
>* *`__extract_keyboard_buttons`: [json](#carouselpy) - This `private` method allows you to prepare the keyboard for adding it to the `carousel` block. It is necessary because the keyboard for the `carousel` cannot contain several buttons `in a row`.*
>
></p></details>
---
### [keyboard.py](keyboard.py)
><details><summary>Class `Keyboard` - The keyboard in messengers is a special type of attachment, unlike ordinary text messages, it is a tool for interactive user interaction with a bot. By clicking on the button, the user gives the system various commands: if these are ordinary buttons, then when clicking on them, the user gives the command to send the text to the community that is written on the button (i.e., the typing process is accelerated), if it is a link or a geo-location, then the system performs these actions outside of a conversation with the bot (sends to the site, sends a placemark on the map).</summary><p>
>
>* `add_button()`: [None](#keyboardpy) - This method adds a button with the type `button_type`, the color `color`, the attachment `payload` and the text `text` at the `right`, to the existing keyboard.
>* `add_line()`: [None](#keyboardpy) - This method moves the `cursor` of the buttons one cell down. I.e., by default, the buttons are added to the row, to the right.
>* `get_keyboard()`: [str](#keyboardpy) - This is json by mind, but it return in the format of a regular string.
>* `get_empty_keyboard()`: [str](#keyboardpy) - This is json by mind, but it return in the format of a regular string.
>
></p></details>

><details><summary>Enum `VkKeyboardButton`</summary><p>
>
>* `DEFAULT`
>* `OPENLINK`
>* `CALLBACK`
>* `LOCATION`
>
></p></details>