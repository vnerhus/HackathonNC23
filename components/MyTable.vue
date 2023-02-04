<template>
    <el-table class="table-striped"
              :data="tableData">
      <el-table-column type="index">
    
      </el-table-column>
      <el-table-column prop="name"
                       label="Name">
      </el-table-column>
      <el-table-column prop="job"
                       label="Job Position">
      </el-table-column>
      <el-table-column prop="salary"
                       label="Salary">
      </el-table-column>
      <el-table-column
        label="Active">
        <template slot-scope="props">
          <base-switch v-model="props.row.active" color="black"></base-switch>
        </template>
      </el-table-column>
    </el-table>
</template>
    
<script>
    import {Table, TableColumn} from 'element-plus'
    export default {
        components: {
            [Table.name]: Table,
            [TableColumn.name]: TableColumn
        },
        data() {
            return {
                tableData: [{
                name: 'Andrew Mike',
                job: 'Develop',
                salary: '€ 99,225',
                active: false
                }, {
                name: 'John Doe',
                job: 'Design',
                salary: '€ 89,241',
                active: false
                }, {
                name: 'Alex Mike',
                job: 'Design',
                salary: '€ 92,144',
                active: false
                }, {
                name: 'Mike Monday',
                job: 'Marketing',
                salary: '€ 49,990',
                active: true
                },
                {
                name: 'Paul dickens',
                job: 'Communication',
                salary: '€ 69,201',
                active: true
                }]
            }
        }
    }
</script>