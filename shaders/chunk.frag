#version 330 core

layout (location = 0) out vec4 fragColor;

const vec3 gamma = vec3(2.2);
const vec3 inv_gamma = 1 / gamma;

in vec4 voxel_color;


void main() {
    fragColor = vec4(voxel_color.xyz, 1);
}






































