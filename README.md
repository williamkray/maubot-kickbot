# kickbot

# this plugin is now deprecated, and its functionality (and improvements!) have been moved into
[communitybot](https://github.com/williamkray/maubot-communitybot)

a maubot plugin that attempts to assist administrators of communities on matrix, based on the concept of matrix spaces.

# features

## activity tracking and reporting

tracks the last message timestamp of a user across any room that the bot is in, and generates a simple report. intended
to be used to boot people from a matrix space and all space rooms after a period of inactivity (prune inactive users)
with the `purge` subcommand.

supports simple threshold configuration and the option to also track "reaction" activity. 

you can also exempt users from showing as "inactive" in the report by setting their ignore status with the `ignore` and
`unignore` subcommands, e.g. `!activity ignore @takinabreak:fromthis.group`. this will be re-set when the user becomes
active again, so this is useful for someone who is going on an extended hiatus! also this is an accident and will
hopefully have a more permanent option in the future as well.

`sync` subcommand will actively sync your space member list with the database to track active members properly. new
members to the space automatically trigger a sync, as do most other commands. this command is mostly deprecated but you
may want to run it just to see what it does.

generate a report with the `report` subcommand (i.e. `!activity report`) to see your inactive users. 

## user management

purge inactive users with the `purge` subcommand (i.e. `!activity purge`).

kick an individual user from your space and all child rooms, regardless of activity status, with the `kick` subcommand
(e.g. `!activity kick @malicious:user.here`). this is useful in communities built on the concept of private (invite
only) matrix spaces.

if you want more sever action, use the `ban` and `unban` subcommands to ban users from all rooms in the space (this action
will automatically kick them from those rooms as well). if you've made a mistake, use the unban option, but they will
need to rejoin all rooms themselves or be re-invited.

use the `guests` subcommand to see who is in a room but NOT a member of the parent space (invited guests) e.g.
`!activity guests #myroom:alias.here`.

# installation

install this like any other maubot plugin: zip the contents of this repo into a file and upload via the web interface,
or use the `mbc` utility to package and upload to your maubot server. 

be sure to give your bot permission to kick people from all rooms, otherwise user management features will not work! for
more robust management, check out the [welcome](https://github.com/williamkray/maubot-welcome),
[join](https://github.com/williamkray/maubot-join), and [createroom](https://github.com/williamkray/maubot-createroom)
plugins as well.
