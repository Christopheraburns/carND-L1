#**Finding Lane Lines on the Road** 



###This was a difficult assignment, after much trial and error and guessing, I have a video that should satisfy the requirements.

---

**Finding Lane Lines on the Road**

The goals of this project are the following:
* Make a pipeline that finds lane lines on the road by taking a video as input and returns an annotated video
* Multiple, helper functions have been included to identify lane lines
* Detected line segments have been extrapolated to connect the dashed lane lines




---

### Reflection

###1. Current Pipeline

I tried to write clear, concise code that minimized code outside of a function.  The provided template already did a pretty good job of that. I did inlcude a single set of variables and eliminated some unnecessary variable passing.

I included a master "processimage" function, that takes, as a parameter the image in an np.array form.  This master function has 6 steps. Each step has at least one corresponding function to encapsulate the procedures of it's respective step in the annotation process.

1.) Convert the image (or video frame) to grayscale
2.) Add a gaussian blur to the image with a kernel of 3 X 3
3.) Apply a canny filter to detect edges.  This filter used thresholds of (low) 50 and (high) 150
4.) Apply an ROI (Region of Interest) mask to remove all edges not part of our lane lines
5.) Apply a Hough transform to annotate lines on the edges detected by the Canny method
6.) Annotate the image (or video frame) 


In order to draw a single line on the left and right lanes, I modified the drawlines() function by calculating the slope of each line and adding those calculations to either a rightline or leftline object.



###2. Identify potential shortcomings with your current pipeline


One potential shortcoming is that i didn't write 90% of this code.  I used the template.  I don't like to do this but this material is not coming easily to me.

The line that I extrapolate has a lot of jitter.  The example video is smooth.  I am not certain how to smooth my line out.

Finally, this video is of a very slow curve.  I don't think this code will work on a sharper curve.


###3. Suggest possible improvements to your pipeline

<<<<<<< HEAD
This code has no error detection/handling

An improvement would be to fix the left lane jitter
=======
A possible improvement would be to fix the left lane jitter
>>>>>>> 7e2b5535d7a27cf0d5712d728d94129caa1f374b

Another potential improvement could be create a library to handle all the grayscale, Canny, and Hough code so I only have to write a wrapper and not recreate the helper functions every time.