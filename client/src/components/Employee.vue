<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Employees Register</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.employee-modal>Add Employee</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Employee ID</th>
              <th scope="col">Name</th>
              <th scope="col">Designation</th>
              <th scope="col">Phone</th>
              <th></th>
            </tr>
            <tr>
              <th scope="col"></th>
              <th scope="col"><input 
              id="search-name" v-model="searchEmployeeForm.name" placeholder="Search by name">
              </input></th>
              <th scope="col"><input 
              id="search-designation" v-model="searchEmployeeForm.designation" placeholder="Search by designation">
              </input></th>
              <th scope="col"><input 
              id="search-phone" v-model="searchEmployeeForm.phone" placeholder="Search by phone">
              </input></th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(employee, index) in employees" :key="index">
              <td>{{ employee.id }}</td>
              <td>{{ employee.name }}</td>
              <td>{{ employee.designation }}</td>
              <td>{{ employee.phone }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-danger btn-sm"  @click="deleteEmployee(employee.id)">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addEmployeeModal"
         id="employee-modal"
         title="Add a new Employee"
         hide-footer>
  <b-form @submit="onSubmit" @reset="onReset" class="w-100">
  <b-form-group id="form-name-group"
                label="Name:"
                label-for="form-name-input">
      <b-form-input id="form-title-input"
                    type="text"
                    v-model="addEmployeeForm.name"
                    required
                    placeholder="Enter name">
      </b-form-input>
    </b-form-group>
    <b-form-group id="form-designation-group"
                  label="Designation:"
                  label-for="form-designation-input">
        <b-form-input id="form-designation-input"
                      type="text"
                      v-model="addEmployeeForm.designation"
                      required
                      placeholder="Enter designation">
        </b-form-input>
      </b-form-group>
      <b-form-group id="form-phone-group"
                  label="Phone:"
                  label-for="form-phone-input">
        <b-form-input id="form-phone-input"
                      type="text"
                      v-model="addEmployeeForm.phone"
                      required
                      placeholder="Enter phone">
        </b-form-input>
      </b-form-group>
    <b-button type="submit" variant="primary">Submit</b-button>
    <b-button type="reset" variant="danger">Reset</b-button>
  </b-form>
</b-modal>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      employees: [],
      addEmployeeForm: {
        name: '',
        designation: '',
        phone: '',
      },
      searchEmployeeForm: {
        name: '',
        designation: '',
        phone: '',
      },
    };
  },
  methods: {
    getEmployees() {
      const path = 'http://localhost:5000/employees';
      axios.get(path)
        .then((res) => {
          this.employees = res.data.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addEmployee(payload) {
        const path = 'http://localhost:5000/addEmployee';
        axios.post(path, payload)
          .then(() => {
            this.getEmployees();
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.log(error);
            this.getEmployees();
          });
    },
    searchEmployee(payload) {
        const path = 'http://localhost:5000/searchEmployee';
        axios.post(path,payload)
            .then((res) => {
            this.employees = res.data.data;
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.log(error);
            this.getEmployees();
          });
    },
    initForm() {
      this.addEmployeeForm.name = '';
      this.addEmployeeForm.designation = '';
      this.addEmployeeForm.phone = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addEmployeeModal.hide();
      const payload = {
        name: this.addEmployeeForm.name,
        designation: this.addEmployeeForm.designation,
        phone: this.addEmployeeForm.phone,
      };
      this.addEmployee(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addEmployeeModal.hide();
      this.initForm();
    },
    deleteEmployee(employeeID) {
    const path = `http://localhost:5000/removeEmployee/${employeeID}`;
    axios.get(path)
      .then(() => {
        this.getEmployees();
        this.message = 'Employee removed!';
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
        this.getEmployees();
      });
    },
  },
   watch: {
    'searchEmployeeForm.name': function(val, oldVal){
      const payload = {
        name: this.searchEmployeeForm.name,
        designation: this.searchEmployeeForm.designation,
        phone: this.searchEmployeeForm.phone,
      };
      this.searchEmployee(payload);
    },
    'searchEmployeeForm.designation': function(val, oldVal){
      const payload = {
        name: this.searchEmployeeForm.name,
        designation: this.searchEmployeeForm.designation,
        phone: this.searchEmployeeForm.phone,
      };
      this.searchEmployee(payload);
    },
    'searchEmployeeForm.phone': function(val, oldVal){
      const payload = {
        name: this.searchEmployeeForm.name,
        designation: this.searchEmployeeForm.designation,
        phone: this.searchEmployeeForm.phone,
      };
      this.searchEmployee(payload);
    },
  },
  created() {
      this.getEmployees();
    }
};
</script>
