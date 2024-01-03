# Lab 3 - Lab 3 -	Low level image processing

## Outline
* Interaction with the keyboard and drawing simple primitives
* Constructing and visualizing histograms
* Contrast-Stretching and histogram equalization
* Thresholding


## Drawing a grid upon an image
Create a new example (`Aula_03_ex_01.py`) that allows superimposing a grid (spacing of 20 pixels) upon an image read from file and displays the resulting image.
If the original image is a gray-level image, the grid should be white.
If the original image is a color (RGB) image, the grid should be gray.
Save the resulting image in a file using the imwrite function.

## Construction and visualization of the histogram of a gray-level image
Compile and test the file `Aula03_exe_02.py`.  
Analyze the code, in particular the following steps:
1.	Defining the features and computing the image histogram.
2.	Computing image features from the histogram.
3.	Creating and displaying an image representing the histogram. On this case the matplotlib is used. As an alternative OpenCV drawing functions could also be used.
Observe what happens when some histogram features are changed: for instance, size (`histSize`) and range of values (`range`).

## Analyzing the histograms of different images
For some of the example images given, analyze their histograms.
Analyze the different features of the image histograms for the image set `ireland-06-*` and classify each one of those images.
 
##	Contrast-Stretching 
Create a new example (`Aula_03_exe_04.py`) that allows applying the Contrast-Stretching operation to a given gray-level image.
The original image and the resulting image should be visualized, as well as the respective histograms.
To accomplish that:
1.	Use the `minMaxLoc` function to determine the smallest and largest image intensity values.
2.	Create a new image that uses the entire range of intensity values (from 0 to 255).
For each image pixel, the intensity of the corresponding pixel in the resulting image is given by:
$$ final(x,y) = {original(x,y) -min  \over max-min} * 255 $$
 

## Optional
Apply the Contrast-Stretching operation to the `DETI.bmp` image and the `input.png` image. 
Visualize the histograms of the different images. What differences do you notice?

##	Histogram-Equalization  
Create a new example (`Aula_03_exe_05.py`) that allows applying the Histogram-Equalization operation to a given gray-level image, using the `equalizeHist` function.
The original image and the resulting image should be visualized, as well as the respective histograms.
Apply the Histogram-Equalization operation to the `TAC_PULMAO.bmp` image. 
What is the difference between the histograms of the original image and the equalized image? 
What does the Histogram-Equalization operation allow?

##	Histograms of RGB images 
Create a new example (`Aula_03_exe_06.py`) that allows visualizing the histogram of each color component of an RGB image, as well as the histogram of the corresponding gray-level image.
Use the `split` function to get the intensity images for each one of the color components.
For some of the example RGB images given, analyze their histograms. 
Visualize the resulting images and the respective histograms.











For starters, create a file, name it `d3_1_1.html` with the following content:
``` html
<html>
    <head>
    </head>
    <body>
         <p>Hello World!</p>
    </body>
</html>
```
To load the D3 library, we must refer to the script source, being served locally or in a CDN. There are 2 versions of D3 simultaneously in every D3 iteration (d3.js and d3.min.js), the main one is better for development purposes, as it can output better error messages and allow navigation of source in-browser, the min version is a deploy version, smaller and usually faster. Alternatively, one can download all the [source repository](https://github.com/mbostock/d3/releases) to make with the source and see the examples. The version used here is 6.5.0 and all the lessons will be tested using this one.
 
To use D3 locally, download the d3.js script from the [D3 website](https://d3js.org/). Place the d3.js in your work directory and use this tag on the `<head>` of your html:

``` html
<script type="text/javascript" src="d3.js"></script>
```

To use the script without direct download:
``` html
<script type="text/javascript" src="https://d3js.org/d3.v6.js"></script>
```
Reload your page, and to verify the correct loading of the library one can use the developer's tools of the browser with `ctrl + shift + i` or `F12` (in Chrome). Choose the source tab and hover over the D3 link, then open a new tab on the browser with source code. Alternatively, on the console tab you can write `d3.` and expect the auto-complete shows available options. Both options can be seen in the following image:

![Correct Loading](./correct_loading.png)

## D3 Selection
The `d3.select()` function selects a DOM node of HTML using the CSS syntax, or `null` on case of non-existant node, and it returns only the first node found. More on CSS selectors [here](https://www.w3schools.com/cssref/css_selectors.asp).

Modify the _Hello_ in the HTML with the following code:
``` html 
<p class="p1" >Hello </p>
``` 
And using the console select the paragraph (`<p>` tag) with the following command:
``` javascript
let elem = d3.select(".p1")
```

Now it is possible to modify the style properties of the node using the command `style`. In the console verify and change the background color with the commands:
``` javascript
elem.style('background-color') // verify color
elem.style('background-color', '#990099') // change color
```

More on selection on the [docs](https://github.com/d3/d3/blob/master/API.md#selections-d3-selection).

## D3 Chaining 

Pay atention that `elem.style()` returns an array. Check that if this array is the same as `elem` using the `===` operator. Most D3 functions return its own selection, allowing chaining of operations. Using selections, change the text of paragraph to "Good morning World!" using the console.

## First Example
Create a new HTML file (`d3_1_3.htm`), with the following content:
``` html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>First D3 Example</title>
        <script type="text/javascript" src="http://d3js.org/d3.v6.js"></script>
    </head>

    <body>
        <script type="text/javascript">
            d3.select("body")
                .append("p")
                .text("New paragraph!");
        </script>
    </body>

</html>
```

In this example D3 chaining is used to add a new paragraph. A alternative way to do the same operations is:
``` javascript
let body = d3.select("body");
let p = body.append("p");
p.text("New paragraph!");
``` 
Load this page and modify the code to add a new paragraph. The new paragraph must have a new color, use the `style` function and the `color` argument.

### Using data
Clear the script tag and use this code:
``` javascript
let dataset = [ 5, 10, 15, 20, 25 ];
		
d3.select("body").selectAll("p")
    .data(dataset)
    .join("p")
        .text("New paragraph!");
```

Now take some time to analyze the code. Pay atention to the dataset definition, and its binding with the paragraphs using the `join` function. Add more elements to the dataset and see what happens.  
To access the array data you need to create a callback function on the element. Change the `text` function to this one with a callback and reload the page.
``` javascript
.text(function (d) {
    return "I can count up to " + d;
});
```

### Styling
Using the `style` function modify the code to bind the color with the array value, black for `d <= 15` and red for `d > 15`. Modify the function used to generate the text and add what is needed. Style other attributes using the data, like the _font-size_ and _margin-left_.(Note that some values need more than the numbers, it needs the metric too,like `font-size: 20px`).

## Bar chart with divs
For this final task of this lesson, we will create a bar chart using the `div` HTML tag. To guarantee that all bars are equal we will define a class and style it using CSS, that way all the divs will share the same set of attributes. The only difference between them will be the size. Add this CSS on the HTML.

``` css
<style type="text/css">
div.bar {
	display: inline-block;
	width: 20px;
	height: 75px; /* Overriden by D3-assigned height on script */
	margin-right: 2px;
	background-color: teal;
}
</style>
```

Now clear the script the D3 selections on the script and add this code:

``` javascript
d3.select("body").selectAll("div")
    .data(dataset)
    .join("div")
        .attr("class", "bar");
```

Analyze the result. To bind the height of the divs with the data a adjustment is necessary:
``` javascript
.style("height", function(d) {
    return d + "px";
});
```

The following small chart is the final result of the script:

![Small Charts](./simple_bars.jpg)

Modify the scale (with a multiplicative factor) and the margin (`margin-right`) to make it more clear. Modify the data and see how it changes the chart automatically. Alternatively you can use code to generate data randomly:
``` javascript
let dataset = []; 
for (var i = 0; i < 25; i++) { 
    let newNumber = Math.random() * 30; 
    dataset.push(newNumber); 
}
```
Most of this last task can be seen on a Mike Bostock [page](https://bost.ocks.org/mike/bar/). A detailed rundown of the workings of join is on the [selection.join page](https://observablehq.com/@d3/selection-join).