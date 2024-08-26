# 02 - Software and Communities: presentations

## Sechedule

Below is the order in which the presentations about software communities will be conducted:

Wednesday (08/21):

* [VS code](../../delivery/VS%20Code.pdf)
* [NeoVim](../../delivery/neovim.pdf)
* [Django](../../delivery/django-slides.pdf)
* [Flask](../../delivery/flask-presentation.pdf)
* [Sklearn](../../delivery/scikit-learn.pdf)

Monday (08/26):

* [TensorFlow](../../delivery/TensorFlow.pdf)
* [OpenCV](../../delivery/OpenCV-Pesquisa.pdf)
* [Blender](../../delivery/Blender.pdf)
* [PostgreSQL](../../delivery/Postgresql.pdf)
* [Pandas](../../delivery/OpenCV-Pandas.pdf)

Each group will have 10 minutes for the presentation and 5 minutes for questions.

## Pull Request 

In order to publish your material, only one member of the group must create a PR where:

* Add your presentation in the folder docs/delivery/
* Edit the achievements file using the command `python dev-aberto.py edit-achievements user`.

You must add a new skill to the file with this format:

```
{
    "skill_id": 2, 
    "metadata": {
        "date": "2024-08-20", 
        "filename": "your file name", 
        "group":["user1","user2","users3"]
        }
}
```

where `["user1","user2","users3"]` is the list of the users that are part of the group.
