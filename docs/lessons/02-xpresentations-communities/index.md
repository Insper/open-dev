# 02 - Software and Communities: presentations

## Sechedule

Below is the order in which the presentations about software communities will be conducted:

Wednesday (08/20):

* [Home Assistant](../../delivery/2025-2/home_assistant.pdf)
* [NeoVim](../../delivery/2025-2/neovim.pdf)
* [Blender](../../delivery/2025-2/blender.pdf)

Each group will have 15 minutes for the presentation and 5 minutes for questions.

## Pull Request 

In order to publish your material, only one member of the group must create a PR where:

* Add your presentation in the folder docs/delivery/2025-2
* Edit the achievements file using the command `python dev-aberto.py edit-achievements user`.

You must add a new skill to the file with this format:

```
{
    "skill_id": 2, 
    "metadata": {
        "date": "2025-08-20", 
        "filename": "your file name", 
        "group":["user1","user2","users3"]
        }
}
```

where `["user1","user2","users3"]` is the list of the users that are part of the group.

*Attention:* if you submit your achievement with **group** metadata, your colleague(s) should **not** do the same, because *dev-aberto* system manages individual points to all group member.
