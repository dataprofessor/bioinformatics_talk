import streamlit as st
import streamlit_book as stb
import numpy as np

from code.trajectory import get_trajectory, fig_from_list

if "trayectory_list" not in st.session_state:
    st.session_state["trayectory_list"] = []

# Title
st.title("Trajectory of a projectile")
st.subheader("Equations of motion of a projectile")
st.latex("x(t) = v_0 \\cos(\\theta)t")
st.latex("y(t) = v_0 \\sin(\\theta)t - \\frac{1}{2} g t^{2}")

# Parameters
st.subheader("Simulation parameters")
c1, c2, c3 = st.columns(3)
dv0 = 1
v0 = c1.slider("Initial Velocity [meters/second]", 
                        min_value=dv0, max_value=100*dv0, 
                        value=10*dv0, step=dv0, help="Initial velocity for the projectile")
dtheta = 1
theta_deg = c2.slider("Initial Angle [degrees]", 
                        min_value=5, max_value=90, 
                        value=45, step=5, help="Initial velocity for the projectile")
# options for gravity: earth, moon, mars, jupiter
gravity_dict = {'Earth': 9.8, 'Moon': 1.6, 'Mars': 3.7, 'Jupiter': 24.8}
gravity_label = c3.selectbox("Gravity", gravity_dict.keys(), index=0)
gravity = gravity_dict[gravity_label]

# Compute the plot
c1, c2 = st.columns([.5, .1])
if c1.button("Add plot"):
    traj_dict = get_trajectory(v0, theta_deg, gravity, gravity_label)
    st.session_state["trayectory_list"].append(traj_dict)

if c2.button("Clear plots"):
    st.session_state["trayectory_list"] = []

if len(st.session_state["trayectory_list"]) > 0:
    fig = fig_from_list(st.session_state["trayectory_list"])
    st.pyplot(fig)

# The quizz
st.subheader("Quizz time!")

stb.single_choice("At what angle is obtained the maximal distance?",
                options=["15", "30", "45", "60", "75"], answer_index=2)

stb.true_or_false("On the moon, the horizontal distance is always larger than on the earth under the same initial velocity and angle.",
                    answer=True)                