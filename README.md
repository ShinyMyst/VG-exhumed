<h2>Basic Plan</h2>

<h3>Description</h3>
Player will take the role of a Necromancer meant to traverse a dungeon.  Battles will take place on a grid.  On either end, there are summoning circles.  Your player character stands on the far left, the enemy on the far right.  The goal is to summon minions to cross the grid and defeat the opposing enemy.  Initially, game will automatically transition between battles with no overworld.

<h3>Combat</h3>
Combat is split into two phases that repeat.
Magic Phase
Minion Phase a 
Minion Phase b

In the magic phase, the player can adjust minions or summon new ones.  In the minion phase, minions will execute their commands.  Minions may have multiple sets of commands.  All minions execute their phase a commands first, then all phase b commands are executed, and so forth until no commands left.  If minion has no later commands, they do nothing.  If units make it all the way to other side of map, they can attack the enemy leader directly if nothing in front of them.

Moving into an enemy could trigger an attack of opportunity.

(Potentially we could go line by line with everything all at once, but that would be harder for player to follow despite more flexibility.)

<h3>Magic</h3>
Primary resource for player will be their mana pool.  Mana is used for casting spells in the mana phase and maintaining minions.  Each magic phase, players regain some mana (possibly an increasing amount as round number goes up).  Upkeep for units is subtracted.  Going over limit may force you to dismiss a minion.  Remaining mana can be used for spells.

The main spell will be to summon a new minion and assign commands, covered in next section.  Some additional options may include, changing a unit's commands/spirits, dismissing a unit, converting an enemy unit on your side of map, attacking a unit, moving a unit.

<h3>Summoning 101</h3>
There are two aspects to summoning a new minion, the vessel and the spirit.  The vessel is the physical body.  Necromancer receives three options - skeleton, zombie, ghoul.  Skeletons do nothing special.  Zombies move when other zombies move.  Ghouls attack when other ghouls attack.

The key element of the game are the spirits.  Rather than having the player select a set of commands, spirits contain a short set of commands.  For example, the deer spirit may move forward twice while the fox may move forward once and attack once.

<h3>Commands</h3>
Commands will be relatively simple for initial tests.  There are 3 main options - move forwards, move laterally, attack.  Moving sideways could vary on direction.

<h3>Spirits</h3>
Spirits in base version will all be animal spirits.  Animal spirits execute basic commands sequentially with no special actions.  Players will be limited by number of spirits they possess.  This will be equivalent to their deck, although they should have access to all of them.


<h2>Requirements</h2>
Here are some requirements to help guide the coding process.

<h3>Classes</h3>
Basic layout stored in the class_outline.drawio

<h3>Required Scenes</h3>
Main Menu
Options Menu
Battle Scene

<h3>Unit Types</h3>
Skeleton - No attributes
Zombie - Moves when other zombies/units move.
Ghoul - Attacks when other ghouls/units attack.

<h2>Additions</h2>
Some other ideas tabled until a working version exists.

- More complicated command sets 
- Conditionals in the command sets
- Additional abilities
- Non-animal spirits
- More vessel types
- More player character types
- Blood mage using HP in place of mana
- Anti-Magic user sumnmoning sphere to reduce enemy regen
- Actual dungeon UI to select pathing

<h2>References</h2>
https://app.diagrams.net/
https://github.com/Mekire/pygame-mutiscene-template-with-movie/tree/master/data/states
https://python-forum.io/thread-336.html
- Game logic pass
- Rendering pass
- Game state contains all the information about where/how to render everything

<h2>To-Do</h2>
<h3>Framework Steps</h3>
~~Test window in Linux Terminal~~
Basic framework added
Create starter scene (0 content required)
Game window boots using starter scene

Image folder with backgrounds/button images
Image dictionary creation
Game window boots with images dictionary created

Add background to starter scene using dict
Game window boots with background

Create a button class
Incorporate button into starter scene
Window boots with button visible
Button changes scenes

More steps
