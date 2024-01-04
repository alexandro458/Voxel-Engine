from vbo import VBO
from shader_program import ShaderProgram


class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}

        # skybox vao
        self.vaos["skybox"] = self.get_vao(
            program=self.program.programs['skybox'],
            vbo=self.vbo.vbos['skybox'])

        self.planet_setters()


    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)])
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()

    def planet_setters(self):
        # earth vao
        self.vaos["earth"] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['earth'])

        # earth vao
        self.vaos["mercury"] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['mercury'])
