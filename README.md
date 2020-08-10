# google-form-automation
Platform for automating Google Form submissions.

## User guide
To get started, simply clone this repository to your computer with 

`git clone https://github.com/jackpalaia/google-form-automation.git`

There are three fields that you will need. The first is the id of the form you are interacting with. This can be found in the URL of the form. The form located at the URL

`https://docs.google.com/forms/d/e/adijasf8has9e8fn-iueah98hdinva8j/viewform`

has an id of `adijasf8has9e8fn-iueah98hdinva8j`. This value can go in the `form_id` variable in `main.py`.

The second variable(s) is the id of each question that you want to fill in the form. To find these, view the form in the browser, right click on the text of the question and select 'inspect element'. This will open a panel to the right of the screen. The div you are looking for is 4 above the selected div. The code will look something like this - 

`<div jsmodel="CP1oW" data-params="%.@.[612126548,&quot;question text &quot;,null,1,[[1825518466,[],true,[],[]]],null,null,null,[]],&quot;i1&quot;,&quot;i2&quot;,&quot;i3&quot;,false]" class="m2">`

You want the number right after the double open bracket `[[`. In my case, this number is `1825518466`.

Repeat this process for each question in the form until you have all the question id's. Then, take these numbers and put them in the `question_numbers` list in `main.py`. Put them in the order of each question.

Finally, for the last field, fill in the `content` list in `main.py` with the content that you want to insert for each question. Again, do this in the order that each question falls in. For example, make sure for the first question, make sure the question id and the content are both the first elements in each respective list.

For multiple choice questions, set the content as the value of the multiple choice option you want to select.

Checkbox questions are currently not supported.

When all previous steps are completed, simply run the program with `python main.py`.