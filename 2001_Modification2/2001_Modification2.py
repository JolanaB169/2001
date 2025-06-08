"""Game 2001 – The PC and the player take turns rolling dice.
Before each throw, the player chooses two dice from the following options: D3, D4, D6, D8, D10, D12, D20, or D100.
The winner is the first to reach 2001 points.
The game was transferred to the server using Flask."""


from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = "moje_tajne_heslo_123"

DICE_SIDES = {
    "D3": 3, "D4": 4, "D6": 6, "D8": 8,
    "D10": 10, "D12": 12, "D20": 20, "D100": 100
}

def roll_die(sides):
    return random.randint(1, sides)

def apply_special_rules(score, roll_sum, turn):
    if turn > 1:
        if roll_sum == 7:
            score //= 7
        elif roll_sum == 11:
            score *= 11
        else:
            score += roll_sum
    else:
        score += roll_sum
    return score

@app.route("/", methods=["GET", "POST"])
def start():
    if request.method == "POST":
        return redirect(url_for("choice"))
    return render_template("start.html")

@app.route("/choice", methods=["GET", "POST"])
def choice():
    if request.method == "POST":
        die1 = request.form.get("die1")
        die2 = request.form.get("die2")
        if die1 not in DICE_SIDES or die2 not in DICE_SIDES:
            return "Please select valid dice!", 400

        # náhodný výběr kostek pro počítač
        c_die1 = random.choice(list(DICE_SIDES.keys()))
        c_die2 = random.choice(list(DICE_SIDES.keys()))

        # počáteční skóre a kolo
        p_score = 0
        c_score = 0
        turn = 1

        return render_template("play.html",
                               p_die1=die1, p_die2=die2,
                               c_die1=c_die1, c_die2=c_die2,
                               p_score=p_score, c_score=c_score,
                               roll_p=0, roll_c=0,
                               turn=turn)
    return render_template("choice.html", dice=DICE_SIDES.keys())

@app.route("/play", methods=["POST"])
def play():
    # načíst skrytá pole
    p_die1 = request.form.get("p_die1")
    p_die2 = request.form.get("p_die2")
    c_die1 = request.form.get("c_die1")
    c_die2 = request.form.get("c_die2")
    p_score = int(request.form.get("p_score"))
    c_score = int(request.form.get("c_score"))
    turn = int(request.form.get("turn"))

    # hod hráče
    roll_p = roll_die(DICE_SIDES[p_die1]) + roll_die(DICE_SIDES[p_die2])
    p_score = apply_special_rules(p_score, roll_p, turn)
    if p_score >= 2001:
        return render_template("result.html", winner="Player", p_score=p_score, c_score=c_score)

    # hod počítače
    roll_c = roll_die(DICE_SIDES[c_die1]) + roll_die(DICE_SIDES[c_die2])
    c_score = apply_special_rules(c_score, roll_c, turn)
    if c_score >= 2001:
        return render_template("result.html", winner="Computer", p_score=p_score, c_score=c_score)

    turn += 1
    return render_template("play.html",
                           p_die1=p_die1, p_die2=p_die2,
                           c_die1=c_die1, c_die2=c_die2,
                           p_score=p_score, c_score=c_score,
                           roll_p=roll_p, roll_c=roll_c,
                           turn=turn)

if __name__ == "__main__":
    app.run(debug=True, port=5070)
