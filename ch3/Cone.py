import vtk

def main():
    colors = vtk.vtkNamedColors()
    colors.SetColor("bkg", [77, 51, 26, 255])

    coneSource = vtk.vtkConeSource()

    mapper = vtk.vtkPolyDataMapper()
    mapper.SetInputConnection(coneSource.GetOutputPort())
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)

    renderer = vtk.vtkRenderer()
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.AddRenderer(renderer)
    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d("bkg"))
    renderWindow.Render()
    renderWindowInteractor.Start()

if __name__ == '__main__':
    main()