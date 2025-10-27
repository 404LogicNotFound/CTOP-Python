from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print('Holaaaaaa a todos los ludopatas de España, hoy estais presentes ante el sorteo más racista del mundo entero, quienes seran los afortunados de que les toque')
print('El primer premiooooooo es *redoble de tambores* es un niño somali de 5 años que su familia fue matada delante suya y tambien sabe un truco especial uno que solo se hace una vez toda la vida, es arabe por si las dudas')
print('El segundo premio es un niño de 8 años que vive en una cueva en Siria y que no ha visto la luz del sol en 3 años, pero es muy listo y sabe hacer magia con las manos, hace la mejor coca de todo el mundo')
print('Y el tercer premio es ser violado en vivo delante nuestra por Didi')
print('Y los afortunados son...')
winners = sample(my_list, 3)
print(f'El primer premio es para el número {winners[0]}')
print(f'El segundo premio es para el número {winners[1]}')
print(f'Y el tercer premio es para el número {winners[2]}')