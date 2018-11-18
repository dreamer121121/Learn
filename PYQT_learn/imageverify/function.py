def load_img(self):
    self.graphicsView.update()
    QApplication.processEvents()
    file_path, _ = QFileDialog.getOpenFileName(self.Form, "选择图片", r".\Demo\test")
    img = QImage()
    img.load(file_path)  # 载入图片
    self.img = img
    self.img = img.scaled(self.graphicsView.width(), self.graphicsView.height())
    self.graphicsView.scene = QGraphicsScene()  # 创建一个图片元素的对象
    self.graphicsView.scene.addPixmap(QPixmap().fromImage(self.img))  # 将加载后的图片传递给scene对象
    self.graphicsView.setScene(self.graphicsView.scene)
