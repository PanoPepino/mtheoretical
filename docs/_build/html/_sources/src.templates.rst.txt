templates
=====================

color\_scheme
----------------------------------

.. automodule:: src.templates.color_scheme
   :members:
   :undoc-members:
   :show-inheritance:

dark\_depths
---------------------------------

.. automodule:: src.templates.dark_depths
   :members:
   :undoc-members:
   :show-inheritance:

.. image:: images/dark_depths_tit.png
   :alt: dark_depths
   :width: 49%

.. image:: images/dark_depths_gen.png
   :alt: dark_depths
   :width: 49%

.. code-block:: python

   #Here you can modify almost all parameters of objects used in these libraries. 
   #In this way you can generate new homogenous templates for your presentations.
   #First you have all the variables. 
   #You can find each of the classes attributes these variables modify down in the file.

   ##### ---- DARK DEPTHS TEMPLATE ---- #####

   #Color of the background
   bg_color= '#ECFEFD'

   #Font color and text size for any text and MathTex
   tex_temp= TexFontTemplates.new_century_schoolbook
   t_size= 30
   t_color= '#011638'

   #Design of all the surrounding boxes (titles, refs, bullet points, vacua and similar) 
   #and general opacities

   #What type of decorator surrounding the main title and section titles
   d_presence_1= "back_frame"
   #What type of decorator surrounding bulleted lists.
   d_presence_2= "box" 
   d_ref= "none" #What type of decorator surrounding references.
   #Notice that refs that do not go to the UR corner 
   #should be individually modified to have a box.
   #Refs have the color of the decorator.
   d_color= '#1348A4' #Color of all decorators
   d_s_w= 0.6 #Stroke width of all decorator and surrounding boxes
   c_rad= 0.1 #Curvature of the corners of such objects
   c_rad_dir_title= [1, 1, 1, 1] #Which corners get curved for titles
   c_rad_dir_boxes= [1, 1, 1, 1] #Same, but for boxes
   f_opa= 0.1 #Opacity of background of things
   tight= 0.4 #How tight is the decorator with respect to the object it contains.
   s_opa= 0.8 #Stroke opacity of the border
   dot_size= 2 #How big the bullet points are

   #Color homogenisation
   h_1= '#742F46'
   h_2= '#9F4160'
   h_3= '#45386B'
   b_color= '#742F46'
   v_color= '#45386B'

   config.background_color= bg_color

   #Definition of Tex defaults. This will change font and its color.
   #Carefull! It seems that there exist some FontTemplates which do not 
   #automatically scale the parenthesis. This drove me crazy for some hours.
   #Be aware of what font you choose.

   Tex.set_default(tex_template= tex_temp)
   MathTex.set_default(tex_template= tex_temp)


fancy\_mint
--------------------------------

.. automodule:: src.templates.fancy_mint
   :members:
   :undoc-members:
   :show-inheritance:

.. image:: images/fancy_mint_tit.png
   :alt: fancy_mint
   :width: 49%

.. image:: images/fancy_mint_gen.png
   :alt: fancy_mint
   :width: 49%

.. code-block:: python

   #Here you can modify almost all parameters of objects used in these libraries. 
   #In this way you can generate new homogenous templates for your presentations.
   #First you have all the variables. 
   #You can find each of the classes attributes these variables modify down in the file.

   ##### ---- FANCY MINT TEMPLATE ---- #####

   #Color of the background
   bg_color= '#EBFFF9'

   #Font color and text size for any text and MathTex
   tex_temp= TexFontTemplates.latin_modern_tw
   t_size= 30
   t_color= '#1C1018'

   #Design of all the surrounding boxes (titles, refs, bullet points, vacua and similar)
   #and general opacities

   #What type of decorator surrounding the main title and section titles
   d_presence_1= "box_long_right"

   #What type of decorator surrounding bulleted lists
   d_presence_2= "box"

   #What type of decorator surrounding references. 
   #Notice that refs that do not go to the UR corner 
   #should be individually modified to have a box. Refs have the color of the decorator.
   d_ref= "none" 
   d_color= '#006661' #Color of all decorators
   d_s_w= 0.1 #Stroke width of all decorator and surrounding boxes
   c_rad= 0.2 #Curvature of the corners of such objects
   c_rad_dir_title= [1, 1, 0, 0] #Which corners get curved for titles
   c_rad_dir_boxes= [1, 1, 1, 1] #Same, but for boxes
   f_opa= 0.1 #Opacity of background of things
   tight= 0.3 #How tight is the decorator with respect to the object it contains.
   s_opa= 0.2 #Stroke opacity of the border
   dot_size= 2 #How big the bullet points are

   #Color homogenisation
   h_1= '#9E4770'
   h_2= '#C49E85'
   h_3= '#EF8354'
   b_color= '#006661'
   v_color= '#006661'

   config.background_color= bg_color

   #Definition of Tex defaults. This will change font and its color.
   #Carefull! It seems that there exist some FontTemplates 
   #which do not automatically scale the parenthesis. 
   #This drove me crazy for some hours. Be aware of what font you choose.

   Tex.set_default(tex_template= tex_temp)
   MathTex.set_default(tex_template= tex_temp)

   #Titles #Note that the corner_rad can be negative!
   #It seems that back_frame fits good both with box in text and nothing as decorator.


