Vue.component('product',{
    props:{
        premium:{
            type:Boolean,
            required:true
        }
    },
    template:`
        <div class="product-info">
        <div><img v-bind:src='image' v-bind:alt="altText"></div>
        <h1>{{ title }}</h1>
        <p v-if="inStock">In Stock</p>
        <p v-else>Out of Stock</p>
        <p v-if="onSale">{{printOut}}
        <p>Shipping: {{shipping}}</p>
        <ul>
            <li v-for="detail in details">{{detail}}</li>
        </ul>
        
        <div v-for="(variant,index) in variants"
            :key="variant.variantId"
            class="color-box"
            :style="{backgroundColor:variant.variantColor}" 
            @mouseover="updateProduct(index)">
        </div>

        <button v-on:click="addToCart" 
            :disabled="!inStock"
            :class="{disabledButton:!inStock}">Add to Cart</button>
     
        <button v-on:click="takeOutFromCart">Take out from Cart</button>
        <product-review></product-review>
    
        </div>
    `,
    data(){
        return {
            brand:"Vue Master",
            product:"Socks",
            description:"A pair of warm fuzzy socks",
            selectedVariant:0,
            altText:"A pair of socks",
            details:["80% cotton","20% polyester","Gender-neutral"],
            variants:[
                {
                    variantId:2234,
                    variantColor:"green",
                    variantImage:"assets\\vmSocks-green-onWhite.jpg",
                    variantQuantity:10
                },
                {
                    variantId:2235,
                    variantColor:"blue",
                    variantImage:"assets\\vmSocks-blue-onWhite.jpg",
                    variantQuantity:0
                }
            ],
            onSale:true
        }
    },
    methods:{
        addToCart(){
            this.$emit('add-to-cart',this.variants[this.selectedVariant].variantId)
        },
        updateProduct(index){
            this.selectedVariant=index
        },
        takeOutFromCart(){
            this.$emit('remove-from-cart',this.variants[this.selectedVariant].variantId);
          
        }
    },
    computed: {
        title() {
            return this.brand + ' ' + this.product
        },
        image(){
            return this.variants[this.selectedVariant].variantImage
        },
        inStock(){
            return this.variants[this.selectedVariant].variantQuantity
        },
        printOut(){
            return this.brand+' '+ this.product
        },
        shipping(){
            console.log(this.premium)
            if(this.premium){
                return "Free"
            }
            return '$2.99'
        }
    }
})

Vue.component('product-review',{
    template:`
        <form class="review-form" @submit.prevent="onSubmit">
        <p>
        <label for="name">Name:</label>
        <input id='name' v-model="name">
        </p>

        <p>
            <label for ="review">Review: </label>
            <textarea id="review" v-model='review'></textarea>
        </p>

        <p>
            <label for="rating"> Rating: </label>
            <select id="rateing" v-model.number='rating'>
                <option>4</option>
                <option>3</option>
                <option>2</option>
                <option>1</option>
                <option>0</option>
            </select>
        </p>

        <p>
            <input type="submit" value="Submit">
        </p>
        </form>
    `,
    data(){
        return {
            name: null,
            review:null,
            rating: null

        }
    }


})


var app=new Vue({
    el:"#app",
    data:{
        premium:false,
        cart:[]            
    },
    methods:{
        updateCart(id){
            this.cart.push(id)
        },
        removeCart(){
            if(this.cart.lenth===0) {
                return 
            }
            else {
                this.cart.pop()
            }
        }
    }
})

