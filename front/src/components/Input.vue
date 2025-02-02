<template>
    <br>
    <div class="input-container">
        <input type="text" @input="updateZapros($event.target.value)">
    </div>
</template>

<style>
.input-container {
    display: flex;
    justify-content: center; /* Center the input horizontally */
}

input {
    width: 60%;
    height: 30px;
    border: 1px solid #ccc;
    border-radius: 20px;
    padding: 5px;
    font-size: 16px;
    color: #333;
    background-color: #fff;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
</style>

<script>
export default {
    props: {
        updateZapros: {
            type: Function,
            required: true
        }
    }
}
</script>
