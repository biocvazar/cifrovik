%from db import Data
%import os


%data = Data('templates/products.db')
%data.select()
%c = 0
%title = "Товари"
<div class='text'>
    <br>
    <br>
    <h1 align='center'>{{title}}</h1>
    <br>
</div>
<div style="position:relative; right:-200px;">
<div class="col-left sidebar"><div class="m-block mb-mana-catalog-leftnav"><div class="block block-layered-nav">
    <div class="block-title">
        <strong><span>Пiдбiр за параметрами</span></strong>
    </div>
    <div class="block-content">
                            <dl id="narrow-by-list">
        <form name="filt" method="get">
                                                                                                    <dt>Ціна</dt>
		<div class="m-slider-values">
		<span id="left_price-range-from" class="m-slider-min-value">Від</span>
                <span id="left_price-applied" class="m-slider-selected-value">
            <input type="text" class="m-slider m-from" name="from" size="2" value="0" /> грн           <br> до            <input type="text" name="to" class="m-slider m-to"size="2" value="0" /> грн        </span>
        	</div>

</dd>
    <dt>Виробник</dt>
                    <dd>
			<ol class="m-filter-css-checkboxes">
				<li >
					<input type="checkbox" name="Canon" value="1">Canon<br>
				</li>
				<li >
					<input type="checkbox" name="Nikon" value="1">Nikon<br>
				</li>
				<li >
					<input type="checkbox" name="Samsung" value="1">Samsung<br>
				</li>

			</ol>

</dd>


</ol>

</dd>
<button type="submit" title="Застосувати" name="filter" class="button btn-cart" value="filter"><span><span>Застосувати</span></span></button>
</form>
</div>
</div>
</div>
</div>
</div>

 <div class="main-container col3-layout">
            <div class="main">
                <div class="col-wrapper">
                    <div class="col-main">
                        <div class="m-block mb-category-products">

<div class="category-products">
<ul class="products-grid">

%i = 0
%for i in range(len(data.rows)):
    %img, name, price = data.rows[i][4], data.rows[i][1], data.rows[i][2]
    %if (i+1)%2 == 0:
        <li class="item">
    %elif (i+1)%3 == 0:
        <li class="item last">
    %else:
        <li class="item first">
    %end


    <a href="/{{name}}" title="{{name}}" class="product-image"><img src="{{'static'+img}}" width="188" height="188" alt="{{name}}" /> </a>
    <h2 class="product-name"><a href="{{name}}" title="{{name}}">{{name}}</a></h2>
    <div class="price-box">
               <span class="regular-price" id="product-price-11075">
               <span class="price">{{price}} грн</span>                                    </span>

        </div>

                <div class="actions">
                <a href="/{{name}}"><button type="button" title="купити" class="button btn-cart" ><span><span>купити</span></span></button></a>
                                </div>
            </li>
    %end
%end


</ul>




</div>
</div>
</div>
</div>
</div>
</div>


