from cmkt.tasks import * 

mytoolkit = TaskToolKit('hineng')

translation_model = mytoolkit.translation(model_name="t5-small")

print(translation_model.get_predictions("yeh achi movie hai"))