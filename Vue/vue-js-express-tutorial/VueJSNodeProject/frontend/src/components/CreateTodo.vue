<template>
<div id="container" class="container">

<div class="row">

<div class="col-sm-8 offset-sm-2">
<div class="alert alert-warning" v-show="showError" >
<button type="button" class="close" @click="hideMessage()">X</button>
<strong>Error!</strong>
</div>
<h1>Create a Todo</h1>

<div class="info-form">
<form>
<div class="form-group">
<label for="name">Todo name</label>
<input v-model="todo.name" type="text" class="form-control" id="name" aria-describedby="nameHelp" placeholder="Enter Name">
<small id="nameHelp" class="form-text text-muted">Enter your todo's name</small>
</div>
</form>

<button class="btn btn-primary" v-if="!this.todo.id" @click="createTodo()" ><span>Create</span>
<button class="btn btn-primary" v-if="this.todo.id" @click="updateTodo()" ><span>Update</span></button>

<button class="btn btn-primary" @click="newTodo()" >New..</button>
</div>
</div>
</div>
</div>
<script>
  import {APIService} from '../APIService';
  const apiServer = new APISerivce();
  export default {
  name: 'CreateTodo',
  


