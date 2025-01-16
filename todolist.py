import json
import flet as ft

def main(page:ft.Page):

    page.scroll = "auto"

    def tarefastsk():
        with open("listtarefas.json", "r") as trfs:
            return json.load(trfs)
        return[]
    tarefas = tarefastsk()
    def salvar():
        with open("listtarefas.json", "w") as trfs:
            json.dump(tarefas, trfs, indent=4)
        

    def att(e, trf):
        for trff in tarefas:
            if trff["Nome"] == trf:
                if trff["Status"] == "Pendente":
                    trff["Status"] = "Concluido"
                    salvar()
                    break
                elif trff["Status"] == "Concluido":
                    trff["Status"] = "Pendente"
                    salvar()
                    break
        paginatarefas()
    
    def adicionar(addnm):
        tarefas.append({"Nome": addnm, "Status": "Pendente"})
        salvar()
        paginatarefas()
    def remover(rmnm):
        for tarefa in tarefas:
            if tarefa["Nome"] == rmnm:
                tarefas.remove(tarefa)
                salvar()
                paginatarefas()
    def paginatarefas():
        page.clean()           
        for tarefa in tarefas:
            if tarefa["Status"] == "Pendente":
                trff = ft.Container(
                    ft.Row(
                        [
                            ft.Text(tarefa["Nome"],color=ft.colors.AMBER_700, size=19, weight="bold"),
                            ft.Text(tarefa["Status"], color=ft.colors.AMBER_700, size=21, weight="italic", text_align="center"),
                            ft.IconButton(icon=ft.icons.CHECK_BOX_OUTLINE_BLANK, on_click=lambda e, trf=tarefa["Nome"]: att(e, trf))
                        
                            #ft.IconButton(icon=ft.icons.CHECK_BOX_OUTLINE_BLANK, on_click=print(tarefa["Nome"]))

                        ],
                        alignment='center',
                        vertical_alignment="center"
                    ),
                    bgcolor=ft.colors.AMBER_ACCENT,
                    alignment=ft.alignment.center
                )
                page.add(trff)
                page.update()
            else:
                trff = ft.Container(
                    ft.Row(
                        [
                            ft.Text(tarefa["Nome"],color=ft.colors.AMBER_700, size=19, weight="bold"),
                            ft.Text(tarefa["Status"], color=ft.colors.AMBER_700, size=21, weight="italic", text_align="center"),
                            #ft.IconButton(icon=ft.icons.CHECK_BOX, on_click=lambda e: att(trf=tarefa["Nome"]))
                            #ft.IconButton(icon=ft.icons.CHECK_BOX_OUTLINE_BLANK, on_click=print(tarefa["Nome"]))
                            ft.IconButton(icon=ft.icons.CHECK_BOX, on_click=lambda e, trf=tarefa["Nome"]: att(e, trf))

                        ],
                        alignment='center',
                        vertical_alignment="center"
                    ),
                    bgcolor=ft.colors.AMBER_ACCENT,
                    alignment=ft.alignment.center
                    )
                page.add(trff)
                page.update()
        nome = ft.TextField(label="Nome", color=ft.colors.BLACK, bgcolor=ft.colors.GREEN, text_align="center")

        addremv = ft.Container(
            ft.Column(
                [
                    nome,
                    ft.ElevatedButton("Remover", color=ft.colors.RED, on_click=lambda e: remover(rmnm=nome.value)),
                    ft.ElevatedButton("Adicionar",color=ft.colors.GREEN, on_click=lambda e: adicionar(addnm=nome.value))

                ],
                alignment="center",
                horizontal_alignment="center"
            ),
            alignment=ft.alignment.center,
            margin=35
        )
        
        page.add(addremv)
    paginatarefas()

ft.app(main)
