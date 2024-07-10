# INVESTMENT INSIGHTS
#### Video Demo:  <URL HERE>
#### Description:

The project provides a concise overview of investments that users might be willing to make. It currently includes Net Present Value (NPV) and the Payback Period. This could make it easier to decide what investment opportunity to take and what investments might not prove as profitable. This is because it also takes into account the time value of money via the discount factor that the user provides. In simple terms, the value of money falls with time.

#### Features

The website currently has only a few features. But I plan on adding more features soon.
The features include:
- Calculation of NPV,
- Calculation of Payback period,
- Visualization of investment insights.

#### Installation

The project has only a few files, and the only part to be addressed is the "requirements.txt".
The website requires "flask" and "calculations" to operate.


**Install dependencies:**

To install the necessary packages, run the following command in your terminal:

   pip install -r requirements.txt


#### Usage

The usage is actually very easy, after the requirements are met, follow this:

1. **Start the website:**

   flask run

2. **Access the website:**
   Open your web browser and go to `http://localhost:5000/`
   (This will be provided by flask)

#### Technologies Used

All technologies used were the one's shown in CS50x.
- Python
- Flask
- Jinja
- Bootstrap
- CSS
- HTML
- Font awesome (This was used for icons and was not a part of CS50x)

#### File Structure

The file structure is very simple and follows what Proffesor David advised:

project/
│
├── app.py            # Main Flask application script
├── calculations.py   # Calculation functions
├── templates/        # HTML templates
├── static/           # Static CSS file
├── requirements.txt  # List of Python dependencies
└── README.md         # Project documentation

#### How I made it

The project started out as a basic structure that I created with the assistance of chatgpt. But the only problem is that the design wasn't good enough to be used anywhere.
So I decided to use Bootstrap to make it look better. I also used Font Awesome for icons.
The calculations were done in a separate file named calculations.py. This made the code cleaner and easier to understand.
The templates were made using Jinja and HTML. The CSS was written in a separate file named style.css in the static folder.

I created a layout.html file to be able to reduce the time of copy pasting all the things between files and then implimented the rest of it.
The rest of the code was written in app.py. This is where the routes were defined and the path to 
"/calculate" was made to be accesable via the "post" method. I didn't see how a "get" method would be beneficial as the page is accesable only via the form submition on the index page (/).

One more goal was to make the website such that it coukd be expanded in the future to add aditional features and also to be launched properly. Hence, the pricing and features (tabs and pages) seemed to be a solid choice.
The website was tested multiple times to ensure that it was working properly.

The final step was to write this README file to explain how the project was made.

This project was made in a total of 5 days: 
The first day was spent on planning. 
The second day was spent on making the basic structure.
The third day was spent on making the design better.
The fourth day was spent on writing the calculations and implimenting them.
The fifth day was spent on testing and writing this README file.

#### Future Improvements

I will continue to add features to this projects. I plan on creating a database and letting users create accounts and store their investment analysis for further comparison. This combined with other financial tools could make this site a future hit.

I will add more features as I learn them. Again, I got the idea from my accounting preprations. In the future as I progress towards a more finance based qualification, I will make sure to add all the things I learn to this website so that many more people (students and professionals alike) could learn and benefit.

#### Contributing

I would appreciate any suggestions and/or contributions to the project. Currently, you can hit me up at my Email or Instagram both of which are on the "contact us" page on the website.

Furthermore, the website also has my github. Now this project isn't on github currently, but I do plan on putting it up on github after I add some more features (I'll do that as I read more chapters). In which case, you could choose to contribute directly via github.

#### License

This does not currently have any license and is free for all to use. I honestly don't understand licenses right now and I'll be looking into them because I plan on making this a large scale website.

#### Acknowledgements

I would like to acknowledge (and thank) many resources that helped my imensely in this project.
None of this would've been possible without them.
- CS50x (Harvard University) for teaching me the basics of web development (and much more).
- Professor David Malan for his guidance and support.
- Stack Overflow for helping me with many errors.
- W3Schools for providing me with many examples and tutorials.
- Bootstrap for providing a great framework for styling.
- Font Awesome for providing icons.
- And many more resources that I used throughout the project.

#### Final words


I did not have much time from my life due to everything else going on. So I had to submit it faster. I'm planning on a type of detox away from my devices. I'd appreciate any feedback and suggestions.

[Email](mailto:msaimbutt799@gmail.com)
[Instagram](https://www.instagram.com/saimbutt799/)
[GitHub](https://github.com/Saimbutt799)

Note: The website is not yet hosted on github. I'll do that soon.

Thank you for reading this README file.
I hope you like the project.
Have a great day!
Sincerely,
Saim <3
