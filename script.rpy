# hi!! welcome to the script file :3 like all these files, i have tried to comment it best i can. some comments are leftover from the project i used as a base for this gui,
# so pls enjoy!!!!!!!!!! ive tried to make it as simple as i can so that you can understand and follow along. do note im a really bad programmer...but im glad u downloaded ts
# in the first place ^_^ anything ive labeled with TODO is just for me to reference when im working on this code in the future. also, i start most of my comments with a single
# hashtag just so you can differentiate them from others

# i also wanna state that this is a forever wip. it will always need tweaks, and anyone who wants to help make things better is welcome, SO welcome as long as yr
# nice and sweet abt it. its up on my github along with my itch, so huzzah!!!!




init python:
   config.nvl_paged_rollback = True

image ctc_animation = Animation("frame1.png", 0.3, "frame2.png", 0.3)
# Declare characters used by this game. i said this on the page but i might as well say it again; there is currently no support for names in this template.
# i've like busted my ass trying to get it to work as i want it to and it does not work in the slightest and still look good. if anyone has ideas on how to implement names,
# please by all means leave a post udner the itch page!!! help is always appreciated
define menu = nvl_menu
define narrator = Character(None, kind=nvl, ctc = "ctc_animation", ctc_pause = "ctc_animation", ctc_timedpause = Null(), ctc_position = "nestled")

## Splashscreen ############################################################
## A portion of the game that plays at launch, before the main menu is shown. 
# all commented out in the nvl gui code, but uncomment it and have fun editing it if u wanna use it ^_^ i kept it in for my own title im using this preset for
## https://www.renpy.org/doc/html/splashscreen_presplash.html

## The animation is boring so I recommend using something else.
## ATL documentation: https://www.renpy.org/doc/html/atl.html

#image splash_anim_1:

#   "gui/renpy-logo.png"
#   xalign 0.5 yalign 0.5 alpha 0.0
#   ease_quad 7.0 alpha 1.0 zoom 2.0

#default persistent.firstlaunch = False

#label splashscreen:
    
#   scene black
#
#  ## Here begins our splashscreen animation.
# show splash_anim_1
   #show text "{size=60}Made with Ren'Py [renpy.version_only]{/s}":
   #  xalign 0.5 yalign 0.8 alpha 0.0
   # pause 6.0
      #linear 1.0 alpha 1.0
    
   ## The first time the game is launched, players cannot skip the animation.
#   if not persistent.seen_splash:
#        
#      ## No input will be detected for the set time stated.
#     ## Set this to be a little longer than how long the animation takes.
#      $ renpy.pause(8.5, hard=True)
#
#      $ persistent.seen_splash = True
    
#   ## Players can skip the animation in subsequent launches of the game.
#   else:
# 
#      if renpy.pause(8.5):
# 
#           jump skip_splash
#
#  scene black
# with fade
 
#  label skip_splash:
#
#    pass
   # 
   #call screen content_warning

   ## The first time the game is launched, players can set their accessibility settings.
   #if not persistent.firstlaunch:

   #  call screen splash_settings

   # call screen preferences

      ## This screen will not appear in subsequent launches of the game when
      ## the following variable becomes true.
      #$ persistent.firstlaunch = True

# return

label start:

   $ renpy.change_language(_preferences.language, force=True)

#this makes it so your audio descriptions appear ! depiction of that later down the line

   scene black
   with fade

   show normalcooluser at scene_center_offleft

   narrator "A young man stands in front of you. He's mildly disheveled, though he has cute horse ears. Isn't that just lovely?"
   narrator "\"Hey.\" He says, quietly, trying to make you feel at least mildly welcome. It's up to you whether he's failing or not, but no matter what, 
   the man still stands."
   # note on this: for dialogue if you decide to write in this style, make sure to put a \ in front of your quotation marks. this makes it so that the dialogue works fine!!!
   narrator "\"Uh...thanks for downloading my GUI. Means a lot.\""
   narrator "\"Yeah yeah, whatever the fuck.\" Bluntly, you push past him. \"Show me Eileen. I want to see Eileen.\""
   ic "test"
   # just a test. if you want to put captions, just use the ic character defined in accessibility!
   show eileen at scene_center_offright

   narrator "Like clockwork, Eileen appears in front of you."

   nvl clear

   # NOW IF UR NOT EXPERIENCED THIS ABOVE THING IS GONNA BE YOUR BREAD AND BUTTER
   # after every couple of entries, you should clear the nvl screen as shown above. currently working on trying to get it to do this automatically, as this really annoying.
   # oh well :P as you have to do it now constantly be checking how stuff looks in your actual game through playtesting. its not too hard i think!

   narrator "\"Hey! It's me! It's Eileen!\" She sings. \"Ask me anything!\""

   narrator "Though satisfied with Eileens apperance, you somewhat want her to say the thing...you know. The thing."
# ignore indentation its FINE it WORKS dont KILL ME...
#choice code is vry janky because i usually write kinetic vns. i dont know how to do choices because i js nevr had to learn. however,
# the good thing is this code does not need to be followed to make your project!!!! i js wanted to say what i said so i didnt get flamed
   menu:
        "Be nice about it.":
            jump nice
        "Be an ass.":
            jump ass

label nice:
   nvl clear

   narrator "Slowly, you clear your throat, and try to be polite as you can."
   narrator "\"It would be cool if you said your quote.\" You spoke in the most polite tone you were able to, and it seemed to make a difference. The horseboy lit up,
   while Eileen just simply kept her smile."
   narrator "\"You've created a new Ren'Py game.\""
   narrator "\"One you add story, pictures, music, you can release it to the world!\""
   narrator "Yes! Yes! She said the thing! She said the fucking thing!!!!!!!"
   narrator "That's all you need. You make your exit with no further issue."
   narrator "Like. Really. All you need. You can stop now bro. Like actually"
return

label ass:
   nvl clear

   narrator "Sadly, you don't know how to behave yourself. I'm too lazy to write the rest right now. I'll handle it later. Dattebayo"







return