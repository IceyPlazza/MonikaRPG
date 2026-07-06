default persistent._monikarpg_unlocked = False
default persistent._monikarpg_first_time = True

# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="Icey_Pizza",
        name="MonikaRPG",
        description="Adds a new RPG minigame to the play tab! (1.0.3 fixed some formatting text boxes, bugfix)",
        version="1.0.3"
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="MonikaRPG",
            user_name="IceyPlazza",
            repository_name="MonikaRPG"
        )