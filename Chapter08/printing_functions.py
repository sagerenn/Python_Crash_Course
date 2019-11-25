def print_models(models,finish_models):
    """print the model, and move the finish list"""
    while models:
        model = models.pop(0)
        print(model)
        finish_models.append(model)

def print_finish_models(finish_models):
    """print the finish models"""
    print("The finish items")
    for finish_model in finish_models:
        print(finish_model)