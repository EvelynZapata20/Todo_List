<template>
  <div>
    <h1>Lista de Tareas</h1>
    <form @submit.prevent="createTask">
      <input v-model="newTaskTitle" placeholder="Nueva Tarea">
      <button type="submit">Agregar</button>
    </form>
    <ul>
      <li v-for="task in tasks" :key="task.id">
        <input type="checkbox" v-model="task.completed" @change="updateTask(task)">
        {{ task.title }}
        <button @click="deleteTask(task.id)">Eliminar</button>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      tasks: [],
      newTaskTitle: ''
    };
  },
  created() {
    this.fetchTasks();
  },
  methods: {
    async fetchTasks() {
      const response = await axios.get('http://127.0.0.1:8000/api/tasks/');
      this.tasks = response.data;
    },
    async createTask() {
      if (!this.newTaskTitle) return;
      const response = await axios.post('http://127.0.0.1:8000/api/tasks/', {
        title: this.newTaskTitle,
        completed: false
      });
      this.tasks.push(response.data);
      this.newTaskTitle = '';
    },
    async updateTask(task) {
      // Corrigiendo la URL y usando comillas invertidas
      await axios.put(`http://127.0.0.1:8000/api/tasks/${task.id}/`, task);
    },
    async deleteTask(taskId) {
      // Corrigiendo la URL y usando comillas invertidas
      await axios.delete(`http://127.0.0.1:8000/api/tasks/${taskId}/`);
      this.tasks = this.tasks.filter(task => task.id !== taskId);
    }
  }
};
</script>
