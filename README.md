# kickbot

a maubot plugin that tracks the last message timestamp of a user across any room that the bot is in, and
generates a simple report. intended to be used to boot people from a matrix space and all space rooms after a period of
inactivity.

supports simple threshold configuration and the option to also track "reaction" activity. you can also exempt
users from showing as "inactive" in the report by setting their ignore status. this will be re-set when the user
becomes active again, so this is useful for someone who is going on an extended hiatus! also this is an accident
and will hopefully be a more permanent design in the future.

sync subcommand will actively sync your space member list with the database to track active members properly. new members
to the space automatically trigger a sync, as do most other commands.

generate a report with the report subcommand. purge users with the purge subcommand.

this plugin is nowhere near finished, there are lots of sharp edges. if you don't feel comfortable reading the code to
understand more what's going on here, please do not use this.
