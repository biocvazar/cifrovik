<div class="frm">
<form name="comm" class="frm" method="get">
<cite class="name_pric">Додати коментар:</cite>
<br>
<cite class="comm_name">Вкажіть своє ім'я:</cite>
<br>
<input type="text" name="comment_name" size="50" maxlength="25">
<br>
<br>
<cite class="comm_name">Напишіть ваш відгук...</cite>
<br>
<textarea type="text" name="comment_text" rows="3" cols="50" size="400" maxlength="400">
</textarea>
<br>
<input type="submit" name="save" value="Прокоментувати" align='left'>
</form>
</div>
<br>

%from db import Data
%data = Data('templates/products.db')
%comments = data.select_com(app)
%data.con.close()
%print (" tempaltes     ", comments)
<div class='text'>
%if comments:
    %for com in comments:
        %cname, ctext = com[2], com[3]
        <div class="comment">
        <spam class="comm_name">{{cname}}</spam>
        <br>
        <cite class="comm_text">{{ctext}}</cite>
        <hr>
        </div>

        <br>
    %end
%end
</div>
