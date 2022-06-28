# kickbot

a maubot plugin that tracks the last message timestamp of a user across any room that the bot is in, and
generates a simple report.

supports simple threshold configuration and the option to also track "reaction" activity. you can also exempt
users from showing as "inactive" in the report by setting their ignore status. this will be re-set when the user
becomes active again, so this is useful for someone who is going on an extended hiatus! also this is an accident
and will hopefully be a more permanent design in the future.

this plugin is nowhere near finished, please ignore until a release is properly cut.
