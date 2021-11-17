<template>
  <div class="home">
<el-container>
  <el-main width="50%">
    <el-row type="flex" justify="end">
      <el-button type="primary" @click='check_template'>检查模板</el-button>
    </el-row>
    <div style="margin: 20px 0;"></div>
    <el-input
      type="textarea"
      autosize
      placeholder="请输入模板定义"
      v-model="template">
    </el-input>
  </el-main>
  <el-main width="50%">
    <el-row type="flex" justify="end">
      <el-button type="success" @click='start_parse'>开始匹配</el-button>
    </el-row>
    <div style="margin: 20px 0;"></div>
    <el-input
      type="textarea"
      autosize
      placeholder="请输入待匹配内容"
      v-model="output">
    </el-input>
  </el-main>

</el-container>

    <el-dialog
      title="提示"
      :visible.sync="dialogVisible"
      width="60%"
      :before-close="handleClose">
      <span>{{result}}</span>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
      </span>
    </el-dialog>

  </div>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      input: '',
      template: '',
      output: '',
      result: '结果',
      dialogVisible: false
    }
  },
  mounted: function() {
      //this.showBooks()
  },
  methods: {
    check_template(){
      this.$axios.post('http://127.0.0.1:8000/api/textparse/check', {
        template: this.template,
      })
        .then((res) => {
            var res = res.data;
            this.dialogVisible = true
            if (res.error_num == 0) {
               // this.template = 'OK'
            } else {
              this.$message.error('新增书籍失败，请重试')
              console.log(res['msg'])
            }
        })
    },
    start_parse(){
      this.$axios.post('http://127.0.0.1:8000/api/textparse/parse', {
        template: this.template,
        'fasd': 1
      })
        .then((res) => {
            var res = res.data;
            this.dialogVisible = true
            if (res.error_num == 0) {
               // this.template = 'OK'
            } else {
              this.$message.error('新增书籍失败，请重试')
              console.log(res['msg'])
            }
        })
    },
    handleClose(done) {
      this.$confirm('确认关闭？')
        .then(_ => {
          done();
        })
        .catch(_ => {});
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
