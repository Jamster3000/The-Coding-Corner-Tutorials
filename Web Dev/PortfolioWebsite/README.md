In this tutorial, you will learn the following things:
- What HTML, CSS and JavaScript is and how they contribute to a website.
- creating a basic Web page with HTML, making it look beautiful with CSS, then using JavaScript to make it interactive.
- How to make your webpage/website accessible for anyone (accessibility is important in a website)
- How to use the developer tools that are built into every Web browser and how they help to understand why your website might not work.
- Finally, this tutorial will also cover some free to use hosting sites/platforms where you can host all your HTML, CSS and JavaScript for free.


## What is a website
A website is a interlinked group of web pages, which can typically be accessed by the internet or by a private website. Websites includes images (and other multimedia), text, links, and any other interactive features.

## What types of websites are there?
1. Single-page Applications (SPA)
These use JavaScript frameworks to load the content dynamically on a single web page without having to reload or create multiple webpages.
**Examples: **Gmail, Trello

2. Progressive Web App (PWA)
These are web apps, a combination of a website and an app in one. These are designed to feel like mobile and desktop applications, which runs as a website. The benefit of this is that it has fast loading from page to page and offline capabilities.
**Examples: **Twitter Lite, George, and Bangle.io

3. Static website
Static websites are ones where the content is fixed and doesn't change unless the source code is manually updated (e.g., JavaScript changes it). We will be working on creating one of these in this tutorial.

4. Dynamic website
Dynamic websites generate content dynamically based on user interaction, preferences, and other inputs. This tutorial won't be covering this because it requires a server.

5. Hybrid website
This is a combination of static and dynamic. The web pages would be static, fixed, but the back-end would fetch data and information from external API's.

6. Headless websites
These websites are where the front-end and the back-end are completely seperate from each other, and internal APIs are used to bind the two together.

__                                                            __

Don't worry too much about these if you don't understand, all you need to know is that this tutorial will cover only static websites.


.

## What is HTML and what is it used for?
**HTML** stands for HyperText Markup Language. This is the language that creatures the structure of the webpage.

> HTML is **NOT** a programming language, HTML has no logic.

HTML has elements, these are little blocks of content on your website, buttons, boxes, inputs, links, etc. These can also be called Tags.

There are approximately 110 tags/elements as of to the newest HTML, you're not expected to memorize them all, you'll likely always have to search up for elements from time to time.

## What is CSS and what is it used for?
**CSS** stands for **C**ascading **S**tyle **S**heets. This is a stylesheet language which is used to describe the presentation of a document. CSS controls how things look; the layout, colours, fonts, spacing, and the overall apperance of your website.

CSS can be a bit messy and it's understandable you may not pick this up right away.

> CSS is also **NOT** a programming language

## What is JavaScript and what is it used for?
JavaScript **IS** a programming language which allows for dynamic, interactive features on a website. This code is client send, meaning that it typically executes in the user's browser rather than servers. 

JavaScript is practically essential in today's websites. JavaScript and webassmebly (WASM) are the only programming languages that directly run in the web browser without additional installations.


> If you couldn't tell, it's really irritating people calling CSS and HTML code or worse, a **programming language** which neither are.

.


## **What is Front-end**
This is a part of web development that focuses on the visuals of what the user sees, buttons, colours, shapes.

## **What is back-end**
 This is the behind-the scenes part. THe processes and functions that make the website work behind what the user sees. It's the whole operation of the website.

## **What is server-side**
Server-side is the code and data that is hosted and executed on a server rather than on the user's/client's computer. **Example** If you search something on Google, those results, links, and images you see - they come from a server somewhere around the world that way millions of GB of data isn't stored on your device.

## **What is client-side**
This is parts of the website that happens on the user's device, rather than on a server. This includes the execution of JavaScript on the user's browser which is delivered from a server (the host of the website) and the browser then renders and processes that code.



__                                                   __

This tutorial is going through everything to create, build, and host your own portfolio website.

## What is a portfolio and a portfolio website?
A **portfolio** is a collection of work or projects that demonstrate your own skills, expertise, and accomplishments.
These are common for professional fields, such as graphic design, programming (web development too), photography, writing and more.

A **portfolio website** is exaclty that, a website that shows (non-private) details about yourself, projects you've made, websites, applications, etc.
Any case studies you may have done
Skills you have
Any achievements, awards, certificates, or other things you've gotten in your field.
A bio about yourself
and even Testimonials.

These are good for different things, esp. as a beginner it's great to have one.
- Demonstrates what you're capable of.
- Show how you visually and interactivly present your website.
- It can help you build a personal brand about yourself and can help you stand out in a competitive world. It shows that you're serious about your work and skills and can provide proof of your abilities, which gives you an upper-hand when trying to get a job or apply for similar roles.

As mentioned above, it can help attract the attention of clients or employers, if you're looking for a job, this type of website can help make you stand out to those sorts of people, having a contact page on your website also helps them easily contact you if they have any interest in what they see.


.



# Setting up your website.
First you need to set up some folders/directories to ensure that all your files are kept neat and tidy.

- Create a new folder somewhere on your device, give it any name you want.

- Inside that folder, create the following:
    - pages
    - css
    - js
    - libs
    - images

As you may have guessed, this keeps things neat and tidy, all your HTML pages go in `pages` folder. JavaScript in `js` folder, and so on.

__                                                           __

Create your first HTML page.
Call this file `index.html`

> DO NOT put this in the `page` folder or any other folder besides the main folder you created. This is usually the only file that doesn't get organized into a. folder.

`index.html` is a standard naming convention, it's normally the homepage to your website. A lot of hosting services and platforms also automatically search for `index.html` too.


Open your index.html file in an IDE, text edit, anything that allows you to type HTML in. You'll see that the file is blank, now we need to create the very basic structure of the HTML.

We are going to keep this HTMl very basic for now and will add to it later on.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to my portfolio website</title>
</head>
<body>
    <header>
    </header>

    <main>
    </main>

    <footer>
    </footer>
</body>
</html>
```

Paste or type this HTMl into your `index.html` file.
Good HTML will have this sort of structure.
Going through it line by line:
- `<!DOCTYPE html>` This just says what type of document this file is.
- `<html lang="en">` this sets the language that is used for the page. "en" is English but you can change it if you prefer.  You can see [here](https://www.w3schools.com/tags/ref_language_codes.asp) for a list of language codes. This also helps with the built in tools for translation in a web browser too.

### head
- Then we head into the <head> tag. There are two groups to a HTML file, the <head> and the <body>. Just like a human head, it contains not structure, but information and metadata.
We are setting just 3 simple things here, although there is a ton more of metadata and other things that can be set here.

- `<meta charset="UTF-8">` - sets the character set or encoding of the file (UTF-8) is most common to use.
- `<meta name="viewport" content="width=device-width, initial-scale=1.0">` - Sets the HTML to take up the entire width and height of the user's screen; dynamic so anyone can view the screen with the right scaling to their screen size.
- `<title>Welcome to my portfolio website</title>` This is also metadata. If you open the html in your browser, you'll see that the name on the tab is the same as what is set for <title>


### body
the body is where all the elements and structure goes. Want a button? goes in the body. Want a input? in the body.

```
<body>
    <header>
    </header>

    <main>
    </main>

    <footer>
    </footer>
</body>
```

You already know the HTML has to groups for different things, <head> for information, <body> for the structure and elements. Inside the <body> you'll see three things that helps split the html up to make it easier to read and find content as it grows in size.

- <header> This actually helps you to create a header on your website (see below for what a header is)
- <main> This is where all your main HTML goes that isn't part of the footer or header.
- <footer> Very similar as the <header> but it acts as the footer instead.

## what is a header on a website?
A header is usually a bar across the top of the webpage which contains key information and navigation to other web pages on website that people would be interested in going to.
Normally, you find on the header:
- A logo
- A name
- Links to other web pages on the website
- account information (e.g., login, sign out)

## what is a footer on a website
The footer is a bar usually across the bottom of the webpage which contains supplementary information or links.
The footer usually contains:
- Basic Copyright information `© 2025 Your Company/name. All rights reserved.`
- Links to your Privacy Policy, Terms & conditions, etc.
- Contact information
- social media links


Don't worry about the header and footer for now. We can work on that next
__                                                     __

> You should try to focus on keeping your HTML in groups and organized as much as possible. Although things like <sections> and <main> are not required and won't affect how your website looks, it's a really good idea to help find the right things in your HTML quickly.



## Header
We're going to keep things simple for the header.
- Logo on the left of the header (keep it simple and use text rather than an actual logo
- a few links for navigation on the right (We will use placeholders for now since we don't have any other pages to go to).

Type the following into your <header> element in your HTML
```html
    <div class="logo">
        <h1>My Portfolio</h1>
    </div>
    <nav>
        <ul>
            <li><a href="#about">About Me</a></li>
            <li><a href="#portfolio">Portfolio</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>
```

> Remember, <header> is nothing more than something to help organize your HTML, it's doesn't format or change the layout as the header (this will require CSS which we will work on later).

- `<div>` This is an empty container, almost like a empty blank element that you can do anything you like with. The class is helpful for CSS and JavaScript. You don't need to worry about that for now.

- <h1> - the "H" is heading. <h1> is the largest heading and <h6> is the smallest.

For the links, we are going to use a <nav> element (meaning navigation).
Inside is a list of links to click on.


## What is a <ul> tag
As you can see from the HTML, the <ul> tag is a list, sort of like an empty box, open and ready to put things inside.

You'll see that there are multiple <li> tags too, these are things that go inside the box, entities that are placed inside the box. But <li> on it's own means nothing they're nothing more than "something" inside the box, we want to say what that "something" is.

This is where our <a> elements come in. You can place any HTML you like in the <li> but since this is a navigation, we only want links. <a> are the link tags (or hyperlink tags if you want to be fancy).

## what is an attribute
Anything you see in the < > of a tag, besids the name of the element's name, is called an attribute.

In the HTML above, we have one attribute called "href" (**Hypertext REFerence,** if you wanted to know what it stood for), this is where you would say what page you're wanting that link to take people. We're using placeholders since we have no other pages to go to. "#" at the start tells the href that it is a placeholder.

__                                                          __

Why not try putting a URL in the href to see it work. E.g. `<a href="www.google.com">Google</a>`

After the first "> You'll see it says "About Me" in the HTML snippet. This is the text to show, which can be anything you want it to be. In fact, it can even be more HTML elements, but let's not get ahead.

> We will use CSS later to make the header look nicer.


.


## main
We're going to work on the main content now. We're going to keep it simple and plain for the time being and add to it later on.
```html
<main>
    <section id="about">
        <h2>About Me</h2>
        <p>Hello! I'm a passionate developer in programming.</p>
        <a href="#about">See more about me!</a>
    </section>
    <section id="portfolio">
        <h2>My Work</h2>
        <p>Here are some of my projects:</p>
        <ul>
            <li>Project 1: <a href="#portfolio">Project One</a></li>
            <li>Project 2: <a href="#portfolio">Project Two</a></li>
        </ul>
    </section>
    <section id="contact">
        <h2>Contact Me</h2>
        <p>Email: yourname@example.com</p>
    </section>
</main>
```

This is a little more cluttered, and I'm sure you're glad that there's more groups in the <main> too!

- `<section>` This defines a section of your HTML, we're using "id" here which just gives that section a name to easily understand (this can be used by CSS and JavaScript too, but that's for later).

- `<a href="#about">See more about me!</a>` you'll see here that we aren't using <nav> or <ul> for a list because we only need one and don't need it as navigation.

You should be able to figure out the rest from here.

## footer
```html
<footer>
        <p>&copy; 2025 [name]. All Rights Reserved.</p>
        <nav>
            <ul>
                <li><a href="https://twitter.com">Twitter</a></li>
                <li><a href="https://github.com">GitHub</a></li>
            </ul>
        </nav>
    </footer>  
```

The footer is pretty simple and easy

- `&copy;` this is just the copy symbol that is rendered on load for you.

You don't have to any links here if you don't want but it's common to find links to external places where they can find your social's and legal policy stuff.


.


## CSS
The current web page looks... ugly? a mess?, right? Well now we're going to use CSS to make it pretty and set the layout to look nice.

First, create a new file called `styles.css`
> this should go in the css folder you have previously created.

First, you are going to need to tell the `index.html` file that you are wanting to use this file as your css.

in the <header> section of your HTML:
```html
<link rel="stylesheet" href="css/styles.css">
```

This looks in the css folder for a file called styles.css. The "rel" just tells it that it should use it to style and make changes to how the HTML appears.


## Header CSS
CSS can be a bit of a mess honestly, I'm sure many here that know css would agree to some extent, but without it, websites would definitely look boring.

> My advise, learn and understand CSS so you can edit and create it but once you're very comfortable with it (which will take time) just get AI to gen a basic template for your CSS and just modify it.

```css
* {
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

header {
    background-color: #333;
    padding: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    padding: 10px;
}

.logo h1 {
    color: #f4f4f4;
    font-size: 24px;
}

nav ul {
    list-style: none;
    display: flex;
    gap: 20px;
}

nav ul li a {
    text-decoration: none;
    color: #f4f4f4;
    padding: 5px 10px;
    transition: color 0.3s ease;
}

nav ul li a:hover {
    color: #007bff;
}
```


This is some CSS for the header. 
It does look like a lot so we'll go through it below.
CSS sets the positions, layouts, colours, shapes, and even animations. Although I will be explaining and showing you CSS it would be good to play around with it see if you can change the colour schemes. (more on what colour schemes are later).

https://www.w3schools.com/cssref/index.php
If this is overwhelming for you, I would not advice taking a look at the link above which lists everything that is available for you to do with CSS.

**For now** let's just go over the CSS for the header.

```css
* {
    margin: 0;
    padding: 0;
}
```

so each block of CSS starts of with the name of an element, this first but is * ||("but that isn't an element name"!)||  This is a reference to all the elements and the entire page.

- Margin - This creates space around elements, in this case, we're setting it to 0, so there is no space around any the elements to start off with, which is good because we can create space around specific elements later on when we need them.

- padding - This adds padding around the element, like an invisible border around the element. In this case, we're also setting this to 0, which we can set for specific elements later on too!

__                                 __

```css
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
}
```

The body is the first element we're referencing in our CSS.
Each line of text on your webpage will sit on a metaphocial line. The line-height just changes this.
and the font-family does as it reads, changes what font you're using.

__                                       __

```css
header {
    background-color: #333;
    padding: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
```

Now we've gotten to the first part of the header's CSS. 
- background-color: we're setting the background color to a dark grey. This uses hex colours, so feel free to play around and see what other colors you like too.
- padding: we're specifically adding padding just to the header to give it a bit of breathing space from all the other elements outside of the header.
- display: the type of layout used.
- justify-content: This tells the browser how it should deal with the space between and around content.
- align-items: Specifies the default alignment for items/elements

__                                                  __

```css
.logo {
    padding: 10px;
}

.logo h1 {
    color: #f4f4f4;
    font-size: 24px;
}
```

These are a little different compared to before. These two start with a "." These are used to target class selectors.
Remember the `class="logo"`? "logo" is the name of a class that we have made up. and in the CSS, we're using "." to say look through the HTMl for all the classes and look for the name "logo" in this instance.

So here, 
```html
<div class="logo">
        <h1>My Portfolio</h1>
    </div>
```
We're just adding 10px padding to all the div.

> If you can't remember what a div is, it's just an empty element container that we can use to make any sorts of elements we want, including just boxes, or visually organizing things.

The next part is `.logo h1`, if that isn't obvious, let's give an example

```html
<div class="logo">
    <h1>My Portfolio</h1>
    <h2>Project 1</h2>
    <h3>Project 2</h2>
    <h4>Project 3</h4>
    <h5>project 4</h5>
</div>
```
Let's pretend that this is in our HTML (it's not, and don't put it in your HTML)
if our CSS was
```css
.logo {
    color: #f4f4f4;
    font-size: 24px;
}
```
It would apply the font-size and color to <h1>, <h2>, <h3> and so on because they are all inside that div with the class called "logo". The colours okay, but the font-size isn't, <h5> is much smaller than \<h1>\ so we can't have them the same font size.

That's where
```css
.logo h1 {
    color: #f4f4f4;
    font-size: 24px;
}
```
comes in. First part you're telling it to apply the colour and font size to the .logo class, then this CSS is only applied to the elements inside the <div> if that element is <h1>.


```css
nav ul {
    list-style: none;
    display: flex;
    gap: 20px;
}

nav ul li a {
    text-decoration: none;
    color: #f4f4f4;
    padding: 5px 10px;
    transition: color 0.3s ease;
}

nav ul li a:hover {
    color: #007bff;
}
```

Finally, our last bit of CSS. 
This is called "descendant selector" because it decends downwards from the parent element (nav) to the smallest element (<a>)
`Navigation` > `List` > `List item` > `Hyper link`

- list-style - we're just making sure it doesn't render bullet points, numbers, or any other sort of points from a list.
- gap - This sets the space between rows and columns, e.g., the space between each <a> in the list.
- text-decoration - Sometimes you'll see a link to click on and it has the little horizontal underline going underneath, setting text-decoration to none will remove that line.
- padding - the first number is top and bottom padding, the second is left and right padding.
- a:hover - You'll see this, which changes the colour on hover. This ":hover" is known as 

### Transition
This can be a fun, simple animation.

When you hover over a link in the <nav> you'll see it change colour. now change 0.3s to a bigger value like 3s you'll see a difference. The transition takes the first argument to be what is changing, this works for dynamic things, so you could have it so the width of the header slowly expands to the full width.

Then you have to specify in time, how long you want it to take. in this case 0.3 seconds is fast.


## CSS Footer
```
footer {
    background-color: #333;
    padding: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: #f4f4f4;
}
```

This css just shares the similar from the header


## CSS Main
Now we are going to apply some CSS for the main content that we currently have.

```css
main {
    max-width: 1200px;
    margin: 0 auto;
    padding: 40px 20px;
}

section {
    margin-bottom: 60px;
    padding: 30px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

section h2 {
    color: #2c3e50;
    font-size: 2em;
    margin-bottom: 20px;
    border-bottom: 2px solid #eee;
    padding-bottom: 10px;
}

section p {
    color: #555;
    line-height: 1.8;
    margin-bottom: 20px;
}

section a {
    color: #3498db;
    text-decoration: none;
    transition: color 0.3s ease;
}

section a:hover {
    color: #2980b9;
}

#portfolio ul {
    list-style: none;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    padding: 0;
}

#portfolio li {
    padding: 20px;
    background: #f8f9fa;
    border-radius: 6px;
    transition: transform 0.3s ease;
}

#portfolio li:hover {
    transform: translateY(-5px);
}

#about {
    display: flex;
    flex-direction: column;
    align-items: start;
}

#contact {
    text-align: center;
}

#contact p {
    font-size: 1.2em;
}
```

This looks a lot but almost all of this contains things we've already covered.

- Look through each element, one by one, and compare it! see what CSS is affecting the <sections>, <main>, etc.

## Reducing number of CSS lines
There are a few things we can do to reduce the amount of lines being used here. The CSS is currently 123 lines in total, and whilst keeping it readable, we are able to reduce it to 106.

__                                                                              __

### 1.
- `color: #f4f4f4;` add this to the header, the header doesn't need it but the footer does
- change `header {` to `header, footer {` with the rest of the CSS staying the same. This creates a basic list of elements so that footer and header in this instance shares the same CSS.
- Remove the original `footer {` block of CSS as we have now reused the header CSS

### 2.
```css
.logo {
    padding: 10px;
}
```
You could remove this if you're not bothered about the logo having much space.

### 3.
```css
#contact {
    text-align: center;
}
```

We can also remove this too since it looks a little silly. It's perfectly fine to experiment with CSS and see what does and doesn't work well.

```css
* {
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

header {
    background-color: #333;
    padding: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo h1 {
    color: #f4f4f4;
    font-size: 24px;
}

nav ul {
    list-style: none;
    display: flex;
    gap: 20px;
}

nav ul li a {
    text-decoration: none;
    color: #f4f4f4;
    padding: 5px 10px;
    transition: color 0.3s ease;
}

ul li a:hover {
    color: #007bff;
}

main {
    max-width: 1200px;
    margin: 0 auto;
    padding: 40px 20px;
}

section {
    margin-bottom: 60px;
    padding: 30px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

section h2 {
    color: #2c3e50;
    font-size: 2em;
    margin-bottom: 20px;
    border-bottom: 2px solid #eee;
    padding-bottom: 10px;
}

section p {
    color: #555;
    line-height: 1.8;
    margin-bottom: 20px;
}

section a {
    color: #3498db;
    text-decoration: none;
    transition: color 0.3s ease;
}

section a:hover {
    color: #2980b9;
}

#portfolio ul {
    list-style: none;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    padding: 0;
}

#portfolio li {
    padding: 20px;
    background: #f8f9fa;
    border-radius: 6px;
    transition: transform 0.3s ease;
}

#portfolio li:hover {
    transform: translateY(-5px);
}

#about {
    display: flex;
    flex-direction: column;
    align-items: start;
}

#contact p {
    font-size: 1.2em;
}
```

You should have something looking like this now. You should also have something similar to what the screenshot looks.
```css
* {
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

header {
    background-color: #333;
    padding: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo h1 {
    color: #f4f4f4;
    font-size: 24px;
}

nav ul {
    list-style: none;
    display: flex;
    gap: 20px;
}

nav ul li a {
    text-decoration: none;
    color: #f4f4f4;
    padding: 5px 10px;
    transition: color 0.3s ease;
}

ul li a:hover {
    color: #007bff;
}

main {
    max-width: 1200px;
    margin: 0 auto;
    padding: 40px 20px;
}

section {
    margin-bottom: 60px;
    padding: 30px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

section h2 {
    color: #2c3e50;
    font-size: 2em;
    margin-bottom: 20px;
    border-bottom: 2px solid #eee;
    padding-bottom: 10px;
}

section p {
    color: #555;
    line-height: 1.8;
    margin-bottom: 20px;
}

section a {
    color: #3498db;
    text-decoration: none;
    transition: color 0.3s ease;
}

section a:hover {
    color: #2980b9;
}

#portfolio ul {
    list-style: none;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    padding: 0;
}

#portfolio li {
    padding: 20px;
    background: #f8f9fa;
    border-radius: 6px;
    transition: transform 0.3s ease;
}

#portfolio li:hover {
    transform: translateY(-5px);
}

#about {
    display: flex;
    flex-direction: column;
    align-items: start;
}

#contact p {
    font-size: 1.2em;
}
```

You should have something looking like this now. You should also have something similar to what the screenshot looks.
```css
* {
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

header {
    background-color: #333;
    padding: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo h1 {
    color: #f4f4f4;
    font-size: 24px;
}

nav ul {
    list-style: none;
    display: flex;
    gap: 20px;
}

nav ul li a {
    text-decoration: none;
    color: #f4f4f4;
    padding: 5px 10px;
    transition: color 0.3s ease;
}

ul li a:hover {
    color: #007bff;
}

main {
    max-width: 1200px;
    margin: 0 auto;
    padding: 40px 20px;
}

section {
    margin-bottom: 60px;
    padding: 30px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

section h2 {
    color: #2c3e50;
    font-size: 2em;
    margin-bottom: 20px;
    border-bottom: 2px solid #eee;
    padding-bottom: 10px;
}

section p {
    color: #555;
    line-height: 1.8;
    margin-bottom: 20px;
}

section a {
    color: #3498db;
    text-decoration: none;
    transition: color 0.3s ease;
}

section a:hover {
    color: #2980b9;
}

#portfolio ul {
    list-style: none;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    padding: 0;
}

#portfolio li {
    padding: 20px;
    background: #f8f9fa;
    border-radius: 6px;
    transition: transform 0.3s ease;
}

#portfolio li:hover {
    transform: translateY(-5px);
}

#about {
    display: flex;
    flex-direction: column;
    align-items: start;
}

#contact p {
    font-size: 1.2em;
}
```

You should have something looking like this now. You should also have something similar to what the screenshot looks.
```css
* {
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

header {
    background-color: #333;
    padding: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo h1 {
    color: #f4f4f4;
    font-size: 24px;
}

nav ul {
    list-style: none;
    display: flex;
    gap: 20px;
}

nav ul li a {
    text-decoration: none;
    color: #f4f4f4;
    padding: 5px 10px;
    transition: color 0.3s ease;
}

ul li a:hover {
    color: #007bff;
}

main {
    max-width: 1200px;
    margin: 0 auto;
    padding: 40px 20px;
}

section {
    margin-bottom: 60px;
    padding: 30px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

section h2 {
    color: #2c3e50;
    font-size: 2em;
    margin-bottom: 20px;
    border-bottom: 2px solid #eee;
    padding-bottom: 10px;
}

section p {
    color: #555;
    line-height: 1.8;
    margin-bottom: 20px;
}

section a {
    color: #3498db;
    text-decoration: none;
    transition: color 0.3s ease;
}

section a:hover {
    color: #2980b9;
}

#portfolio ul {
    list-style: none;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    padding: 0;
}

#portfolio li {
    padding: 20px;
    background: #f8f9fa;
    border-radius: 6px;
    transition: transform 0.3s ease;
}

#portfolio li:hover {
    transform: translateY(-5px);
}

#about {
    display: flex;
    flex-direction: column;
    align-items: start;
}

#contact p {
    font-size: 1.2em;
}
```

You should have something looking like this now. You should also have something similar to what the screenshot looks.

https://media.discordapp.net/attachments/1325800516487352461/1329107408626122774/image.png?ex=67a57b7b&is=67a429fb&hm=e47594574fbd7416f268d5e7afffe0460f16ceef32f9723085dfd5ee00cb0b06&=&format=webp&quality=lossless&width=1534&height=1082


---

# What can you do with your website next?
- Create more pages, this definitely isn't finished yet. You can change the <a href> element to link to your other pages (e.g., `<a href="pages/about">About</a>` will navigate the user to the about.html file if present in the **pages** folder.

- Look into adding a contact form to your website. You can use https://formsubmit.co/ for example in a <form> element to create a working email based contact without needing a server.

- Change the CSS and make it look prettier, currently this is bland and boring, there's no excitement and doesn't show anything, so change it up, maybe you want to use purple and gold colour instead, it's all up to you. Perhaps even add animation, make things move and pop.

- Continue following the tutorial below to get a quick guide on the sort of things you could include in a portfolio website

# What things would be included in a portfolio website?
- Your name and profession (Ideally best on your home page), a brief sentence or two that summaries your skills and values up - and "call-to-action" buttons, such as a button to go to the contact page for example.

- **About**: 
    - You could include an introduction of who you are, your background, and your expertise
    - Your key skills and areas of specialization.
    - Achievements or Credentials you have.
    - if you feel it's appropriate, you could include hobbies and interests too.

- **Projects**: You could select a few important ones or have them all in a grid format.
    - Title & Description
    - Skills/technologies used
    - Links to live Demos (videos) or repositories
    - Any challenges you may have faced.

- **CV/Resume**: DO NOT put a downloadable file or a preview of your actual CV as it can contain (or at least it is supposed to) contain personal and private details that not just anyone should be able to access online. 
Although optional, you could create a summary of your CV, taking out phone numbers, email addresses, addresses, etc.

- **Contact**: 
    - Email address (or a contact form if you prefer instead of having your email visible to anyone)
    - Socials (e.g., Twitter(X 🙄 ), Github, Linkedin)

- **Blogs/Articles** (Optional) Completely optional but you could put a few blogs or articles on if you wanted.

- **Testimonials** (optional): This is feedback you have gotten from people. Quotes from clients, colleagues, or employers.

- **Picture** (optional): It's up to you whether you want to add a picture of yourself to your own portfolio website, adding a picture builds trust to anyone that sees your portfolio.

# free to use hosting services
- GitHub Pages - Very easy to use.
- Firebase - Moderate difficulty


- Netlify - Easy to use
- Vercel - Easy to use
- AWS lambda - Moderate difficulty

There are of course plenty of others but these are the popular ones.
This tutorial will only cover GitHub Pages & Firebase just to keep it short, but you can always create your own tutorial on other hosting services or ask for a tutorial on them if you prefer.

# GitHub
This will use GitHub Pages. If you're on a regular free version of GitHub, you'll have to have a public repository. If you have GitHub Pro, GitHub Education, etc. you are able to use GitHub pages with private repositories too!

1. Create a repository and make it public - The name of your repository will be the name of your website's domain (e.g., https://[yourUsername].github.io/[repositoryName])
2. In your repository, head into `Settings`
3. In the left sidebar go onto `Pages`

https://media.discordapp.net/attachments/1325800516487352461/1336994796274712648/Screenshot_2025-02-06_at_09.39.35.png?ex=67a5d4ef&is=67a4836f&hm=13bea3cc723d0b006e1528fa770a95aaaae1de86d2ddd80013e8594c3c05b992&=&format=webp&quality=lossless&width=2268&height=388


Under `Branch` on that page, you'll see where it says `None` - `Save` Change the `None` to `Main` or whatever the primary branch your using is.

> Make sure to save it!


__                                                                       __

Head back to the code tab, on the top left. `Add Files` > `Upload Files`. Here upload all your website's files and folders.

Once uploaded, if you head to the `Actions` tab in GitHub, You'll see the processes that are going on to make your site live. This should take no more than a few minutes to become live site, although it isn't unknown for it to take longer.

 __                                                                       __

There are ways to add your own custom domain, but that will require you to pay for one, and this tutorial is more based on the free side of things.

.



# Firebase
## Setup
- Install [Nodejs](https://nodejs.org/en/download)
- Install Firebase CLI - Open Terminal, run `npm install -g firebase-tools`
- Create an account with firebase - Head to [Firebase website](https://firebase.google.com/) and make sure you have an account (e.g., using your Google account).

## Initialization
Back to the terminal: 
- Run `firebase login` This will allow you to login into the cli tool securely.

Once logged in >
Create a folder that your website files will be hosted in, and make sure your terminal is in this directory.

**Finally**
Run `firebase init hosting`in your terminal. This will go through the setup for your project. This will present you with options and questions for your project.

- When presented with the question to choose a Firebase project, you can choose to create a new one, or choose one you have already setup in the Firebase console online.

- Keep the default hosting directory as `public` which will be the folder that firebase reads to upload all your hosting files.

- Unless you're create Single-Page App (SPA) - which just plain JavaScript, HTML, and CSS isn't, set this to No.

- ideally, if you're prompted to rewrite the index.html, it's advised not to. You'll be writing this yourself anyway.

__                                                                                      __

Add all your website files to `/public` or whatever the folder you choose was.
Once you're ready, use the command `firebase deploy` in the terminal, it'll upload the files to your project on firebase and host them.


If you are developing your site, you can use the command `firebase serve` this will host your files as a website (like normal) but just on localhost, which is perfect for testing and developing without affecting the final product).

__                                                                                      __


## What makes Firebase any different.
Although it has a paid tier for additional features, you get a lot of free features that most sites don't offer.

Here's some of the best free stuff that most static sites seem limited with.

- Authentication: You can implement creating accounts,, forgot passwords, logging in, etc. securely for users. Firebase stores these accounts for your in their server. This can include several different sign-in options. password & email, Facebook, Google, Twitter, etc.
- Remote Config: A feature where it allows you to set variables with a value that your site can read from. This is useful for changing parts of your website without having to update the code and re deploy it. (e.g., you can set a variable to False to disable a certain feature in your website, or change a string to update your website's colour).
- Web app hosting: You can host web application with firebase, which isn't so simple for most free hosting options.
- 10 GB storage: You have storage for your website files up to 10 GB, although your visitors don't have any storage unless you implement third party storage.
- Realtime Database: Although you don't have storage for user's, the realtime database is basically storage for users (in a sense) - It's NOSQL (see it as a similar thing to JSON), where you have limited storage but since it's just text you likely won't have a lot to worry about.

There is a lot more that I haven't covered here, this is just a start though.
You can take a look at https://family-weaver.web.app which is a perfect, minimal example of the login authentication provided by firebase, and includes remote config for being able to update and change the announcement bar text.
