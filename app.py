from flask import Flask, render_template, request
import cpf

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def home_page():
    ''' Function to handle with inputs in HTML page in CPF checker'''
    if request.method == "POST":
        cpf_number_input = request.form["cpfv"]

        if cpf.check_cfp(cpf_number_input)[0]:
            cpf_number_input_format = ''
            cpf_number_input_format += cpf_number_input[:3] + "."
            cpf_number_input_format += cpf_number_input[3:-5] + "."
            cpf_number_input_format += cpf_number_input[6:-2] + "-"
            cpf_number_input_format += cpf_number_input[9:]

            return render_template('home.html',
                                    content=[cpf.check_cfp(cpf_number_input),
                                    cpf_number_input_format],
                                    example_cpf=cpf.generate_cpf()[1])
        else:
            return render_template('home.html',
                                    content=[cpf.check_cfp(cpf_number_input), ''],
                                    example_cpf=cpf.generate_cpf()[1])
    cpf_number_input = ''
    return render_template('home.html',
                            content=['GET', ''],
                            example_cpf=cpf.generate_cpf()[1])


@app.route('/cpf-generator', methods=["POST", "GET"])
def cpf_generator():
    ''' Function to format and show cpf generate in cpf generate function '''
    if request.method == "POST":
        cpf_generated_list = cpf.generate_cpf()
        cpf_number_generate = cpf_generated_list[1]
        cpf_number_generate_format = ''
        cpf_number_generate_format += cpf_number_generate[:3] + "."
        cpf_number_generate_format += cpf_number_generate[3:-5] + "."
        cpf_number_generate_format += cpf_number_generate[6:-2] + "-"
        cpf_number_generate_format += cpf_number_generate[9:]

        return render_template('cpf-generator.html',
                                content=[cpf_generated_list[0],
                                cpf_generated_list[1] ,
                                cpf_number_generate_format])

    return render_template('cpf-generator.html',
                            content=['', ''])

@app.route('/info')
def info_page():
    ''' Function to render template to info page '''
    return render_template('info.html')

@app.route('/cnpj-validator')
def cnpj_validator():
    ''' Function under development, future cpnj validator '''
    return render_template('cnpj-validator.html')


app.run()
