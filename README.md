# polybius
After watching this youtube documentary about the hoax of the polybius arcade machine, I took the end to task.

https://www.youtube.com/watch?v=_7X6Yeydgyg

In it, the youtuber finds some interesting information pointing towards the creation of the urban legend in 2000 by the owner of coinop.com to stir up traffic. Upon confronting him with the information, the owner says that the wording on the page is "very deliberate"

The page in question is here: http://www.coinop.org/Game/103223/Polybius

Of note so far I found the following:

* The original page text when authored (according to waybackmachine) did not have the information after "quick update" so I am ignoring this as part of the code. 
* There is a spelling error of "disappeard" despite everything else being correct and the youtuber pointing out that the page author corrected spelling of wikipedia pages about the urban legend
* Using tools at http://rumkin.com/tools/cipher/cryptogram-solver.php for "disappeard" that yields "SIXTEENTHS" as a ROT cryptogram - possible wrong path but who knows
* Using other tools at http://rumkin.com/tools/cipher/manipulate.php and pasting all text above the "quick update" and removing spaces, using a 10 character offset will make "disappeard" fit perfectly
* Looking at the current source code of the page and doing a diff against other pages on coinop, nothing stands out as a source code change on the page. I'm using the current state of the page, not waybackmachine caches as the site owner said word choice matters

So I wrote some python code to start to analyze things. Nothing of use yet.

Then I found this reddit page: https://www.reddit.com/r/gamedetectives/comments/6z1ukv/not_exactly_arg_help_solve_the_polybius_mystery/
