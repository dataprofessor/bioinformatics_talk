import streamlit as st
import numpy as np

from code.trajectory import get_trajectory, fig_from_list, check_solution

# Fill up the page
c1, c2 = st.columns([8,1])
c1.title("The Game")
restart = c2.button("Restart")

# Gravity constants by planet
GRAVITY_DICT = {'Earth': 9.8, 'Moon': 1.6, 'Mars': 3.7, 'Jupiter': 24.8}

# Setup the session_state variables
if restart or "remaining_guesses" not in st.session_state:
    st.session_state["remaining_guesses"] = 3

if restart or"guess_list" not in st.session_state:
    st.session_state["guess_list"] = []

if restart or"game_gravity_index" not in st.session_state:
    st.session_state["game_gravity_index"] = np.random.randint(0, len(GRAVITY_DICT))
planet_list = list(GRAVITY_DICT.keys())
game_planet = planet_list[st.session_state["game_gravity_index"]]
game_gravity = GRAVITY_DICT[game_planet]

if restart or "solution" not in st.session_state:
    v0_sol = np.random.randint(30, 60)
    theta_deg_sol = 45
    theta_rad_sol = theta_deg_sol * np.pi / 180
    t_max_sol = 2*v0_sol*np.sin(theta_rad_sol)/game_gravity
    x_max_sol = v0_sol*np.cos(theta_rad_sol)*t_max_sol
    pig_position = [x_max_sol, 0]
    st.session_state["solution"] = {
                                    "pig_position":pig_position, 
                                    "v0_sol": v0_sol, 
                                    "theta_deg_sol": theta_deg_sol,
                                    }

article_dict = {'Earth': "", 'Moon': "the", 'Mars': "", 'Jupiter': ""}
c1.subheader(f"Can you hit the target on {article_dict[game_planet]} {game_planet}?")

# Pig position
x_text = f"x = {st.session_state.solution['pig_position'][0]:.3f} meters"
y_text = f"y = {st.session_state.solution['pig_position'][1]:.3f} meters"
st.write(f"The target is at **{x_text}** and **{y_text}**")
# Get the parameters
st.subheader("Enter the parameters")
c1, c2, c3, c4 = st.columns([3,3,3,1])
dv0 = 1
v0 = c1.slider("Initial Velocity [meters/second]", 
                        min_value=dv0, max_value=100*dv0, 
                        value=50, step=dv0, help="Initial velocity for the projectile")
dtheta = 1
theta_deg = c2.slider("Initial Angle [degrees]", 
                        min_value=5, max_value=90, 
                        value=30, step=5, help="Initial velocity for the projectile")
# options for gravity: earth, moon, mars, jupiter
c3.metric(value=game_gravity, label=f"{game_planet}'s gravity in m/s^2")

# Shoooooot
if st.session_state["remaining_guesses"] > 0:
    if c4.button("Shoot!"):
        st.session_state["remaining_guesses"] -= 1
        traj_dict = get_trajectory(v0, theta_deg, game_gravity, game_planet)
        st.session_state["guess_list"].append(traj_dict)

# Placeholder for information
placeholder = st.empty()

# Always plot, to show the target
fig = fig_from_list(st.session_state["guess_list"], st.session_state.solution["pig_position"])
st.pyplot(fig)

# We check if we hit the pig after the shoot we have guesses left
if check_solution(st.session_state.solution["pig_position"], st.session_state["guess_list"]):
    placeholder.success("You hit the pig... I mean, the target!")
elif st.session_state["remaining_guesses"] == 0:
    line1 = "You're out of guesses! :("
    v0_sol = st.session_state.solution["v0_sol"]
    theta_deg_sol = st.session_state.solution["theta_deg_sol"]
    line2 = f"One possible solution was $v_0$={v0_sol} [m/s^2] and $\\theta$={theta_deg_sol} [deg]"
    placeholder.error(line1 + line2)
else:
    # Say to keep trying, but only if at least tried once
    if st.session_state['remaining_guesses']==2:
        text = f"Keep trying! You have {st.session_state['remaining_guesses']} guesses remaining. Have you tried solving the equations?"
        placeholder.warning(text)
    if st.session_state['remaining_guesses']==1:
        text = f"Use carefully the last guess!"
        placeholder.warning(text)            